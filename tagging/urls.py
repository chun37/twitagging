from django.urls import path

from tagging.views import tag

urlpatterns = [
    path("", tag.IndexView.as_view(), name="index"),
    path("tags/create/", tag.CreateTagView.as_view()),
    path("tags/", tag.TagListView.as_view()),
]
