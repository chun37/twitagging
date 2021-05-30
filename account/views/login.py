from django.views.generic import TemplateView
from django.shortcuts import render


class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        print("request")
        return super().get(request, *args, **kwargs)