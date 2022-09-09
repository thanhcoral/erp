from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from common.permissions import group_required

@group_required('SubAdmin', 'HR', raise_exception=True)
def human_resources(request):
    context = {}
    return render(request, 'pages/human-resources.html', context)

@group_required('SubAdmin', 'HR', raise_exception=True)
def add_user(request):
    context = {}
    return render(request, 'functions/human_resources/add-user.html', context)