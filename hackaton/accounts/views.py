from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout
from django.contrib import messages

def user_logout(request):
    logout(request)
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = UserProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserProfileCreationForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Регистрация'})