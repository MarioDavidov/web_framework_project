from django.contrib.auth import login
from django.shortcuts import render, redirect


from authentication.forms import RegisterForm


def register_user(request):
    if request.method == 'GET':
        context ={
            'user_form': RegisterForm()
        }
        return render(request, 'home_page.html', context)
    else:
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form = user_form.save()

            login(request, user_form)
            return redirect('home_page.html')

        context = {
            'user_form': user_form,

        }
        return render(request, 'home_page.html', context)
