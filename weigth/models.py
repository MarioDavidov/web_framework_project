from django.db import models
from authentication.models import UserProfile


class Weight(models.Model):
    date = models.DateTimeField()
    weight = models.CharField(max_length=5)

    # user = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
