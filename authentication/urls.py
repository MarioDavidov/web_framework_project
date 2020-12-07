from django.urls import path

from authentication.views import register_user

urlpatterns = [
    path('', register_user, name='register_user'),

]
