from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                ("text", models.TextField(verbose_name="Текст")),
                ("category", models.CharField(max_length=100, verbose_name="Категория")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")),
            ],
            options={"verbose_name": "статья", "verbose_name_plural": "статьи", "ordering": ["-created_at", "-pk"]},
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Имя")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("message", models.TextField(verbose_name="Сообщение")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")),
            ],
            options={"verbose_name": "отзыв", "verbose_name_plural": "отзывы", "ordering": ["-created_at", "-pk"]},
        ),
    ]
