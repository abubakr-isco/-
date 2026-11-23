from django.urls import path

from . import views


urlpatterns = [
    path("", views.article_list, name="article_list"),
    path("articles/new/", views.article_create, name="article_create"),
    path("articles/<int:pk>/", views.article_detail, name="article_detail"),
    path("articles/<int:pk>/edit/", views.article_edit, name="article_edit"),
    path("feedback/", views.feedback, name="feedback"),
]
