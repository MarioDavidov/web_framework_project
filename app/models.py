from django.contrib.auth.models import User
from django.db import models

from authentication.models import UserProfile


class Workout(models.Model):
    tittle = models.CharField(max_length=20)
    date = models.DateField()
    first_exercise = models.CharField(max_length=40, blank=True)
    second_exercise = models.CharField(max_length=40, blank=True)
    third_exercise = models.CharField(max_length=40, blank=True)
    fourth_exercise = models.CharField(max_length=40, blank=True)
    fifth_exercise = models.CharField(max_length=40, blank=True)
    notes = models.TextField(max_length=200, blank=True)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)



class ProgressPicture(models.Model):
    date = models.DateField()
    comment = models.TextField(max_length=100, blank=True)
    progress_picture = models.ImageField(
        upload_to='Progress_pics',
        blank=True)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

