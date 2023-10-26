from django import forms
from .models import User, Messages
from django.contrib.auth.forms import AuthenticationForm


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = "__all__"
