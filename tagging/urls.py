from django.urls import path

from tagging import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tags/create/", views.CreateTagView.as_view()),
    path("tags/", views.TagListView.as_view()),
]
