from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from authentication.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_pic',)