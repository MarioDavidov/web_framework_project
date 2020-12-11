from django.urls import path

from app.views import home_page, edit_workout, workouts, \
    create_workout, DeleteWorkoutView, details_workout

urlpatterns = [
    path('home/', home_page, name='home_page'),
    #path('create/', CreateWorkoutView.as_view(), name='create_workout'),
    path('create/', create_workout, name='create_workout'),
    path('edit/<int:pk>/', edit_workout, name='edit_workout'),
    path('delete/<int:pk>/', DeleteWorkoutView.as_view(), name='delete_workout'),
    #path('delete/<int:pk>/', delete_workout, name='delete_workout'),
    path('details/<int:pk>/', details_workout, name='details_workout'),
    path('workouts/', workouts ,name ='workouts'),
    #path('workouts/', WorkoutsView.as_view() ,name ='workouts')
]
