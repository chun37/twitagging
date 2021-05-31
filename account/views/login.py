from urllib.parse import parse_qsl

from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from requests_oauthlib import OAuth1Session

from account.models import Twitter
from twitter_wrapper import TwitterAPI


class LoginView(View):
    def get(self, request, *args, **kwargs):

        oauth_callback = "http://127.0.0.1:8000/accounts/callback/"

        twitter = OAuth1Session(
            settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET_KEY
        )

        request_token_url = "https://api.twitter.com/oauth/request_token"

        response = twitter.post(
            request_token_url, params={"oauth_callback": oauth_callback}
        )

        request_token = dict(parse_qsl(response.content.decode("utf-8")))

        authenticate_url = "https://api.twitter.com/oauth/authenticate"
        authenticate_endpoint = "%s?oauth_token=%s" % (
            authenticate_url,
            request_token["oauth_token"],
        )

        return redirect(authenticate_endpoint)


class CallbackView(TemplateView):
    def get(self, request, *args, **kwargs):
        oauth_token = request.GET.get("oauth_token")
        oauth_verifier = request.GET.get("oauth_verifier")

        if oauth_token is None or oauth_verifier is None:
            raise ValueError

        twitter = OAuth1Session(
            settings.TWITTER_API_KEY,
            settings.TWITTER_API_SECRET_KEY,
            oauth_token,
            oauth_verifier,
        )

        access_token_url = "https://api.twitter.com/oauth/access_token"

        response = twitter.post(
            access_token_url, params={"oauth_verifier": oauth_verifier}
        )

        token_response = dict(parse_qsl(response.content.decode("utf-8")))

        access_token = token_response["oauth_token"]
        access_token_secret = token_response["oauth_token_secret"]
        user_id = token_response["user_id"]
        screen_name = token_response["screen_name"]

        twitter_obj, _ = Twitter.objects.get_or_create(
            access_token=access_token,
            access_token_secret=access_token_secret,
            defaults={"screen_name": screen_name},
        )

        user_model = get_user_model()
        user_model.objects.get_or_create(id=user_id, defaults={"twitter": twitter_obj})

        profile, json = TwitterAPI(
            settings.TWITTER_API_KEY,
            settings.TWITTER_API_SECRET_KEY,
            access_token,
            access_token_secret,
        ).get_user_from_id(user_id)

        twitter_obj.raw = json
        twitter_obj.display_name = profile.name
        twitter_obj.save()

        return render(request, "login.html")
