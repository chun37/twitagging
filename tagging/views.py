from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "about.html")
        return super().get(request, *args, **kwargs)
