from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

from .forms import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                # request.session.set_expiry(86400)
                login(request, user)
                return render(request, 'index.html')
            else:
                return redirect("/auth/login")
        else:
            pass
        
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)

@login_required
def logout_view(request):
    pass

def forbidden(request):
    context = {}
    return render(request, '403.html', context)