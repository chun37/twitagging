from typing import Any, Dict, List

from django.http.request import HttpRequest
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get(
        self, request: HttpRequest, *args: List[Any], **kwargs: Dict[str, Any]
    ) -> TemplateResponse:
        if not request.user.is_authenticated:
            return render(request, "about.html")
        return super().get(request, *args, **kwargs)
