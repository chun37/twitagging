from django import forms
from django.core.validators import MaxLengthValidator, validate_slug

from tagging.models import Tag


class TagForm(forms.Form):
    name = forms.CharField(validators=[MaxLengthValidator(25, "25文字以内で入力してください。")])
    description = forms.CharField(required=False)
    is_private = forms.BooleanField(required=False)
