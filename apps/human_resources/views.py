from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from common.permissions import group_required
from termcolor import colored

from apps.authentication.forms import RegisterForm2
from apps.human_resources.utils import lv

@group_required('Sub Admin', 'HR', raise_exception=True)
def human_resources(request):
    context = {}
    return render(request, 'pages/human-resources.html', context)

@group_required('Sub Admin', 'HR', raise_exception=True)
def add_user(request):
    form = RegisterForm2(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            
            recent_group = request.user.groups.first().name
            request_group = form.cleaned_data.get('groups')
            if lv(recent_group) >= lv(request_group):
                context = {
                    'form': form,
                    'err': 'You do not have permission add user at position: ' + request_group,
                }
                return render(request, 'functions/human_resources/add-user.html', context)

            # user = form.save()
            # group = Group.objects.get(name=request_group)
            # user.groups.add(group)
            context = {
                    'form': form,
                    'err': 'OK:',
                }
            return render(request, 'pages/human-resources.html', context)
        else:
            print(colored('form is not valid', 'red'))
    
    return render(request, 'functions/human_resources/add-user.html', context)
