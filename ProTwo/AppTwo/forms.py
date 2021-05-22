from AppTwo.models import User
from django import forms
from django.forms import ModelForm
from django.core import validators


class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
       