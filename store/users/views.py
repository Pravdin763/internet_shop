from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages

from users.models import User
from users.forms import UserLoginForm, UserRegisterationForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method=='POST':
        form = UserRegisterationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы зарегестрированы')
            return HttpResponseRedirect('/')
    else:
        form= UserRegisterationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)

def profile(request):
    if request.method =='POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)    # instance=request.user - конкретный пользователь   files=request.FILES - передаем смену изображения
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserProfileForm(instance=request.user)       # instance=request.user - конкретный пользователь
    context = {"title": 'store - профиль', 'form': form}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')