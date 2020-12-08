from django.urls import path

from app.views import home_page, create_workout, edit_workout, delete_workout, details_workout

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('home/create/<int:pk>/', create_workout, name='create_workout'),
    path('home/edit/<int:pk>/', edit_workout, name='edit_workout'),
    path('home/delete/<int:pk>/', delete_workout, name='delete_workout'),
    path('home/details/<int:pk>/', details_workout, name='details_workout'),

]
