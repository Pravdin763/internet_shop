from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth

from users.models import User
from users.forms import UserLoginForm, UserRegisterationForm


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
            return HttpResponseRedirect('/')
    else:
        form= UserRegisterationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context)