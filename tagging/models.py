from allauth.socialaccount.models import SocialAccount
from django.db import models

# Create your models here.


class Tag(models.Model):
    list_id = models.BigIntegerField()
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
