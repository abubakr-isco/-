from django.test import TestCase
from django.urls import reverse

from .models import Article, Feedback


class BlogTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title="Первая статья", text=" ".join(f"слово{i}" for i in range(25)), category="Python"
        )

    def test_list_and_detail_show_article(self):
        response = self.client.get(reverse("article_list"))
        self.assertContains(response, "Первая статья")
        self.assertContains(response, "слово19")
        self.assertNotContains(response, "слово24")
        self.assertContains(response, self.article.created_at.strftime("%d.%m.%Y"))
        self.assertContains(self.client.get(self.article.get_absolute_url()), "Первая статья")

    def test_create_requires_valid_title(self):
        url = reverse("article_create")
        response = self.client.post(url, {"title": " аб ", "text": "Текст", "category": "Django"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "не менее 5 символов")
        self.assertEqual(Article.objects.count(), 1)

        response = self.client.post(url, {"title": "Новая статья", "text": "Текст", "category": "Django"}, follow=True)
        self.assertEqual(Article.objects.count(), 2)
        self.assertContains(response, "Статья создана")

    def test_edit_updates_existing_article(self):
        response = self.client.post(
            reverse("article_edit", args=[self.article.pk]),
            {"title": "Исправленная статья", "text": "Новый текст", "category": "Новости"},
        )
        self.assertRedirects(response, self.article.get_absolute_url())
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, "Исправленная статья")
        self.assertEqual(Article.objects.count(), 1)

    def test_feedback_saves_and_shows_success(self):
        url = reverse("feedback")
        response = self.client.post(url, {"name": "Али", "email": "ali@example.com", "message": "Спасибо"}, follow=True)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertContains(response, "Ваше сообщение сохранено")

    def test_feedback_rejects_bad_email(self):
        response = self.client.post(reverse("feedback"), {"name": "Али", "email": "bad", "message": "Спасибо"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "email", html=False)
        self.assertEqual(Feedback.objects.count(), 0)
