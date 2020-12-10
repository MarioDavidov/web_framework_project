from django.db import models

from authentication.models import UserProfile


class Workout(models.Model):
    tittle = models.CharField(max_length=20)
    date = models.DateField()
    first_exercise = models.CharField(max_length=30)
    second_exercise = models.CharField(max_length=30)
    third_exercise = models.CharField(max_length=30)
    fourth_exercise = models.CharField(max_length=30)
    fifth_exercise = models.CharField(max_length=30)
    notes = models.TextField(max_length=200)

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


