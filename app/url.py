from django.urls import path

from app.views import home_page, edit_workout, workouts, \
    DeleteWorkoutView, details_workout, create_progress_picture, progres_picture, DeletePictureView, \
    create_workout, calculator

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('calculator/', calculator, name='calculator'),
    #path('create/', CreateWorkoutView.as_view(), name='create_workout'),
    path('create/', create_workout, name= 'create_workout'),
    path('edit/<int:pk>/', edit_workout, name='edit_workout'),
    path('delete/<int:pk>/', DeleteWorkoutView.as_view(), name='delete_workout'),
    #path('delete/<int:pk>/', delete_workout, name='delete_workout'),
    path('details/<int:pk>/', details_workout, name='details_workout'),
    path('workouts/', workouts ,name ='workouts'),
    #path('workouts/', WorkoutsView.as_view() ,name ='workouts')

    #path('create/progres_picture/', CreateProgressPicture.as_view(), name='create_progress_pic'),
    path('create/progres_picture/', create_progress_picture, name='create_progress_pictures'),
    #path('create/progres_picture/', ListProgressPicture.as_view(), name='progress_pictures')
    path('progres_picture/', progres_picture, name= 'progress_picture'),
    path('picture/delete/<int:pk>/', DeletePictureView.as_view(), name='delete_progress_picture'),



]
