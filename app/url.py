from django.urls import path

from app.views import home_page, create_workout, edit_workout, delete_workout, details_workout, workouts

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('create/', create_workout, name='create_workout'),
    path('edit/<int:pk>/', edit_workout, name='edit_workout'),
    path('delete/<int:pk>/', delete_workout, name='delete_workout'),
    path('details/<int:pk>/', details_workout, name='details_workout'),
    path('workouts/', workouts ,name ='workouts')
]
