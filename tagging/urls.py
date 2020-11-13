from django.urls import path

from tagging import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("create_tag/", views.CreateTagView.as_view()),
]
