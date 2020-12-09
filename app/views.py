from django.shortcuts import render, redirect

from app.forms.workout import WorkoutForm
from app.models import Workout


def home_page(request):
    return render(request, 'home/home_for_users.html')

def workouts(request):
    return render(request, 'workouts.html')

#NxBhej_4g+KBw9YQ
def create_workout(request):
    #workout = Workout.objects.get(pk =pk)
    if request.method == 'GET':
        context = {
            'form': WorkoutForm(),
        }
        return render(request, 'create_workout.html', context)
    else:
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        context = {
            'form': WorkoutForm(),
        }
        return render(request, 'workouts.html', context)


def edit_workout(request):
    pass


def delete_workout(request):
    pass


def details_workout(request):
    pass
