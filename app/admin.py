from django.contrib import admin
from app.models import Workout, ProgressPicture


class WorkoutsInLine(admin.StackedInline):
    model = Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'id','user')
    inlines = (WorkoutsInLine)

admin.site.register(Workout)
admin.site.register(ProgressPicture)