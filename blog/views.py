from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArticleForm, FeedbackForm
from .models import Article, Feedback


def article_list(request):
    return render(request, "blog/article_list.html", {"articles": Article.objects.all()})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "blog/article_detail.html", {"article": article})


def article_create(request):
    form = ArticleForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        article = form.save()
        messages.success(request, "Статья создана.")
        return redirect(article)
    return render(request, "blog/article_form.html", {"form": form, "heading": "Новая статья"})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, instance=article)
    if request.method == "POST" and form.is_valid():
        article = form.save()
        messages.success(request, "Статья обновлена.")
        return redirect(article)
    return render(request, "blog/article_form.html", {"form": form, "heading": "Редактировать статью", "article": article})


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        Feedback.objects.create(**form.cleaned_data)
        messages.success(request, "Спасибо! Ваше сообщение сохранено.")
        return redirect("feedback")
    return render(request, "blog/feedback.html", {"form": form})
