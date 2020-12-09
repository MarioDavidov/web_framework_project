from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from authentication.forms import RegisterForm, LoginForm, ProfileForm
from authentication.models import UserProfile

#2475vbh=@2&L6SdH
#N?b62_%K+LUxQN8b
#NxBhej_4g+KBw9YQ
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
            return redirect('current user profile')
        return redirect('current user profile')


def register_user(request):
    if request.method == 'GET':
        context ={
            'form': RegisterForm(),
        }
        return render(request, 'home_page.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()###

            profile = UserProfile(user=user, )
            profile.save()

            login(request, user)
            return redirect('registered')

        context = {
            'form': form,
        }
        return render(request, 'home_page.html', context)





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

            if user:
                login(request, user)
                return redirect('registered')
        context = {
            'login_form': login_form,
        }
        return render(request, 'login_logout/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home_page')
