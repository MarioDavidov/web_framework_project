from django.contrib import admin

# Register your models here.
from app.models import Workout, ProgressPicture

admin.site.register(Workout)
admin.site.register(ProgressPicture)