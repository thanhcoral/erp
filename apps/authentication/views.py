from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import LoginForm, RegisterForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'test.html')
            else:
                return redirect("/auth/login")
        else:
            pass
        
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            return redirect("/auth/login")
        else:
            pass
        
    context = {
        'form': form,
    }
    return render(request, 'auth/register.html', context)