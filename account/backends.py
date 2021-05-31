from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class OAuthBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        return kwargs["user"]

    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(id=user_id)
        except user_model.DoesNotExist:
            return None
