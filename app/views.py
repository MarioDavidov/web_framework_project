from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from app.forms.progress_picture import ProgressPictureForm
from app.forms.workout import WorkoutForm
from app.models import Workout, ProgressPicture
from django.views import generic as views

from authentication.models import UserProfile


def home_page(request):
    return render(request, 'home/home_for_users.html')


"""
class WorkoutsView(views.ListView):
    model = Workout
    template_name = 'workouts.html'
    context_object_name = 'workout'
"""


def workouts(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if Workout.objects.exists():
        workout = Workout.objects.all()
        context = {
            'workout': workout,
            'profile_user': user,
            'profile': user.userprofile,
            'workouts_user': user.userprofile.workout_set.all(),
        }
        return render(request, 'workouts.html', context)
    else:
        workout = Workout.objects.all()
        context = {
            'workout': workout
        }
        return render(request, 'workouts.html', context)


# 2021-03-21 --> fucking valid date
# NxBhej_4g+KBwasdasd --> pass for user "Mario"
# NxBhej_4g+KBwasdasd --> pass for user "Mario2"
# $AU2QdtJt5re7mQ&
# NxBhej_4g+KBwasdasd

def create_workout(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    # WorkoutForm.user = user
    if request.method == 'GET':

        context = {
            'form': WorkoutForm(),
            'profile_user': user,
            'user_id': user.id,
        }

        return render(request, 'create_workout.html', context)
    else:
        form = WorkoutForm(request.POST)

        if form.is_valid():
            work = form.save(commit=False)
            work.user = request.user.userprofile
            work.save()
            return redirect('workouts')
        context = {
            'form': WorkoutForm(),
            'profile_user': user,
            'user_id': user.id,
        }
        return render(request, 'workouts.html', context)


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


def edit_workout(request, pk=None):
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
            # 'profile_user': user,
            'form': form
        }
        return render(request, 'workouts.html', context)


class DeleteWorkoutView(views.DeleteView):
    model = Workout
    template_name = 'delete_workout.html'
    success_url = reverse_lazy('workouts')


def details_workout(request, pk):
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


"""PICTURES VIESW START FROM HERE"""

"""
class ListProgressPicture(views.ListView):
    model = ProgressPicture
    template_name = 'progress_pictures/progress_pictures.html'
    context_object_name = 'progress_picture'
"""
"""
class CreateProgressPicture(views.CreateView):
    template_name = 'progress_pictures/create_progress_picture.html'
    model = ProgressPicture
    form_class =  ProgressPictureForm
"""


def progres_picture(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if ProgressPicture.objects.exists():
        progress_picture = ProgressPicture.objects.all()
        context = {
            'progress_picture': progress_picture,
            'profile_user': user,
            'profile': user.userprofile,
            'progress_picture_user': user.userprofile.progresspicture_set.all(),

        }
        return render(request, 'progress_pictures/progress_pictures.html', context)
    else:
        progress_picture = ProgressPicture.objects.all()
        context = {
            'progres_picture': progress_picture,
        }
        return render(request, 'progress_pictures/progress_pictures.html', context)


def create_progress_picture(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form_pic': ProgressPictureForm(),
            'profile_user': user,
        }
        return render(request, 'progress_pictures/create_progress_picture.html', context)
    else:
        form = ProgressPictureForm(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user.userprofile
            form.save()
            return redirect('progress_picture')
        context = {
            'form_pic': ProgressPictureForm(),
        }
        return render(request, 'progress_pictures/progress_pictures.html', context)


class DeletePictureView(views.DeleteView):
    model = ProgressPicture
    template_name = 'progress_pictures/delete_progress_pic.html'
    success_url = reverse_lazy('progress_picture')

# U*whCB6Q!48Y+B%@

# hG=%@X!yKkE3%HJ?asd
