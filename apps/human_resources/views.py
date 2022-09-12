from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from common.permissions import group_required
from termcolor import colored

from apps.authentication.models import User
from apps.human_resources.forms import EditForm, RegisterForm2
from apps.human_resources.utils import lv


@group_required('Sub Admin', 'HR', raise_exception=True)
def human_resources(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'pages/human_resources/human-resources.html', context)

@group_required('Sub Admin', 'HR', raise_exception=True)
def add_user(request):
    form = RegisterForm2(request.POST or None)
    users = User.objects.all()
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
                return render(request, 'pages/human_resources/add-user.html', context)

            user = form.save()
            group = Group.objects.get(name=request_group)
            user.groups.add(group)
            context = {
                    'users': users,
                    'form': form,
                    'err': 'OK:',
                }
            return render(request, 'pages/human_resources/human-resources.html', context)
        else:
            print(colored('form is not valid', 'red'))
    
    return render(request, 'pages/human_resources/add-user.html', context)

@group_required('Sub Admin', raise_exception=True)
def delete_user(request, pk):
    users = User.objects.all()
    try:
        user = User.objects.get(id=pk)
    except:
        context = {
            'users': users,
            'err': 'User not exist'
        }
        return render(request, 'pages/human_resources/human-resources.html', context)
    User.objects.filter(id=pk).delete()
    context = {
        'users': users,
        'mess': 'Delete successfully'
    }
    return render(request, 'pages/human_resources/human-resources.html', context)

@group_required('Sub Admin', raise_exception=True)
def edit_user(request, pk):
    user = User.objects.get(id=pk)
    form=EditForm(instance=user)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form=EditForm(request.POST, instance=user)
        form.fields['password1'].initial = user.password
        form.fields['password2'].initial = user.password
        print(form)
        if form.is_valid():
            recent_group = request.user.groups.first().name
            request_group = form.cleaned_data.get('groups')
            if lv(recent_group) >= lv(request_group):
                context = {
                    'form': form,
                    'err': 'You do not have permission edit user at position: ' + request_group,
                }
                return render(request, 'pages/human_resources/edit-user.html', context)

            user = form.save()
            group = Group.objects.get(name=request_group)
            user.groups.add(group)
            users = User.objects.all()
            context = {
                    'users': users,
                    'form': form,
                    'err': 'Edit OK',
                }
            return render(request, 'pages/human_resources/human-resources.html', context)
        else:
            print(colored('form is not valid', 'red'))
    return render(request, 'pages/human_resources/edit-user.html', context)