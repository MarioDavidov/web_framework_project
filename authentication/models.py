from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_pic = models.URLField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
