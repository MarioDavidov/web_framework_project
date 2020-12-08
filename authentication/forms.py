from django import forms
from django.contrib.auth.models import User

from authentication.models import UserProfile


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('profile_pic',)