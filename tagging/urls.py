from django.urls import path
from tagging.views import index

app_name = "tagging"

urlpatterns = [
    path("", index.IndexView.as_view(), name="index"),
]