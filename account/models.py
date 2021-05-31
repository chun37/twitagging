from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class Twitter(models.Model):
    screen_name = models.CharField(max_length=255, default="")
    display_name = models.CharField(max_length=255, default="")

    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)

    raw = models.TextField()


class UserManager(BaseUserManager):
    def _create_user(self, password, **extra_fields):
        user = self.model(**extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, **extra_fields):
        return self._create_user(**extra_fields)

    def create_superuser(self, **extra_fields):
        extra_fields.setdefault("is_admin", True)

        return self._create_user(**extra_fields)


class User(AbstractBaseUser):
    id = models.BigIntegerField(primary_key=True)
    twitter = models.OneToOneField(Twitter, on_delete=models.CASCADE, null=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "id"

    @property
    def is_staff(self):
        return self.is_admin

    def has_module_perms(self, _):
        return self.is_admin

    def has_perm(self, *_):
        return self.is_admin

    def __str__(self):
        return str(self.id)
