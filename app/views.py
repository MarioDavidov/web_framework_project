from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from app.forms.workout import WorkoutForm
from app.models import Workout
from django.views import generic as views
from authentication.views import user_profile


def home_page(request):
    return render(request, 'home/home_for_users.html')
"""
class WorkoutsView(views.ListView):
    model = Workout
    template_name = 'workouts.html'
    context_object_name = 'workout'
"""
def workouts(request,pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if Workout.objects.exists():
        workout = Workout.objects.all()
        context ={
            'workout': workout,
            'profile_user': user,
            'profile': user.userprofile,
            'workouts_user': user.userprofile.workout_set.all(),
        }
        return render(request, 'workouts.html',context)
    else:
        workout = Workout.objects.all()
        context= {
            'workout': workout
        }
        return render(request, 'workouts.html',context)


#NxBhej_4g+KBwasdasd
#$AU2QdtJt5re7mQ&
#NxBhej_4g+KBwasdasd

def create_workout(request):
    if request.method == 'GET':
        context = {
            'form': WorkoutForm(),
        }
        return render(request, 'create_workout.html', context)
    else:
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workouts')
        context = {
            'form': WorkoutForm(),
        }
        return render(request, 'home/home_for_users.html', context)
"""
class CreateWorkoutView(views.CreateView):
    template_name = 'create_workout.html'
    model = Workout
    form_class = WorkoutForm

    def get_success_url(self):
        url = reverse_lazy('workouts',kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        workout = form.save(commit=False)
        workout.user = self.request.user.userprofile
        workout.save()
        return super().form_valid(form)
"""

def edit_workout(request,pk):
    workout = Workout.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'workout': workout,
            'form': WorkoutForm(instance=workout),

        }
        return render(request, 'edit_workout.html', context)
    else:
        form = WorkoutForm(request.POST, instance=workout)

        if form.is_valid():
            form.save()
            return redirect('workouts')
        context = {
            'workout': workout,
            'form': form
        }
        return render(request, 'workouts.html', context)

class DeleteWorkoutView(views.DeleteView):
    model = Workout
    template_name = 'delete_workout.html'
    success_url = reverse_lazy('workouts')

"""
def delete_workout(request):
    pass
"""

def details_workout(request ,pk):
    workout = Workout.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'workout': workout,
            'form': WorkoutForm(instance=workout),

        }
        return render(request, 'workout_details.html', context)
    else:
        workout = Workout.objects.get(pk=pk)
        context = {
            'workout': workout,

        }
        return render(request, 'home/home_for_users.html', context)