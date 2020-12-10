from django.shortcuts import render, redirect

from app.forms.workout import WorkoutForm
from app.models import Workout


def home_page(request):
    return render(request, 'home/home_for_users.html')

def workouts(request):
    if Workout.objects.exists():
        workout = Workout.objects.all()
        context ={
            'workout': workout,
        }
        return render(request, 'workouts.html',context)
    else:
        workout = Workout.objects.all()
        context={
            'workout': workout
        }
        return render(request, 'workouts.html',context)


#NxBhej_4g+KBw9YQ
#$AU2QdtJt5re7mQ&
def create_workout(request):
    #workout = Workout.objects.get(pk =pk)
    if request.method == 'GET':
        context = {
            'form': WorkoutForm(),
        }
        return render(request, 'create_workout.html', context)
    else:
        form = WorkoutForm(request.POST)
        #
        if form.is_valid():
            form.save()
            return redirect('workouts')
        context = {
            'form': WorkoutForm(),
        }
        return render(request, 'home/home_for_users.html', context)


def edit_workout(request):
    pass


def delete_workout(request):
    pass


def details_workout(request):
    pass
