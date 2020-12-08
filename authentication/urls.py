from django.urls import path

from authentication.views import register_user, login_user, logout_user, user_profile

urlpatterns = [
    path('profile/', user_profile, name="current user profile"),
    path('profile/<int:pk>/', user_profile, name="user profile"),
    path('', register_user, name='register_user'),
    path('login/', login_user, name = 'login_user'),
    path('', logout_user, name = 'logout_user'),
    path('home/', register_user, name = 'registered'),

]
