from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {}
    return render(request, 'index.html', context)