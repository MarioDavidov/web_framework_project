from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from authentication.forms import RegisterForm, LoginForm, ProfileForm
from authentication.models import UserProfile


def register_user(request):
    if request.method == 'GET':
        context ={
            'user_form': RegisterForm(),
        }
        return render(request, 'home_page.html', context)
    else:
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form = user_form.save()

            profile = UserProfile(user=user_form, )
            profile.save()

            login(request, user_form)
            return redirect('registered')

        context = {
            'user_form': user_form,
        }
        return render(request, 'home_page.html', context)

def user_profile(request, pk =None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'form': ProfileForm(),
        }
        return render(request, 'home/home_for_users.html',context)
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('curent user profile')
        return redirect('curent user profile')


def login_user(request):
    if request.method == "GET":
        context = {
            'login_form': LoginForm(),
        }
        return render(request, 'login_logout/login.html', context)
    else:
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password,)

            if user or user is None:
                login(request, user)
                return redirect('registered')
        context = {
            'login_form': login_form,
        }
        return render(request, 'login_logout/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home_page')
