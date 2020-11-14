from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from allauth.socialaccount.models import SocialToken

from tagging.models import Tag
from tagging.forms import TagForm
from tagging.twitter_api import Twitter

# Create your views here.


class Create(LoginRequiredMixin, FormView):
    form_class = TagForm
    template_name = "tags/create.html"
    success_url = "/"

    def form_valid(self, form):
        social_token: SocialToken = SocialToken.objects.get(
            account__user=self.request.user.id
        )

        api = Twitter(
            social_token.app.client_id,
            social_token.app.secret,
            social_token.token,
            social_token.token_secret,
        )
        tag = api.create_list(
            form.cleaned_data["name"],
            form.cleaned_data["description"],
            form.cleaned_data["is_private"],
        )

        Tag(
            list_id=tag.id, account=social_token.account, name=form.cleaned_data["name"]
        ).save()

        return super().form_valid(form)


class List(LoginRequiredMixin, ListView):
    template_name = "tags/list.html"

    def get_queryset(self):
        return Tag.objects.filter(account__user=self.request.user.id)
