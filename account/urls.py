from django.contrib.auth import views as auth_views
from django.urls import path

from account.views import login

app_name = "accounts"

urlpatterns = [
    path("login/", login.LoginView.as_view(), name="login"),
    path("callback/", login.CallbackView.as_view(), name="callback"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
