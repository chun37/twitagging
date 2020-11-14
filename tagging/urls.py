from django.urls import path

from tagging.views import tag, views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("tags/create/", tag.Create.as_view()),
    path("tags/", tag.List.as_view()),
]
