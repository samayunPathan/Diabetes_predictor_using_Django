from django import forms
from django.core import validators
from predictor import models


class UserForm(forms.ModelForm):
    class Meta:
        model=models.User
        fields="__all__"
class DataForm(forms.ModelForm):
    class Meta:
        model=models.predictor_data
        fields="__all__"