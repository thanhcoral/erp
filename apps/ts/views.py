from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from common.permissions import group_required

@group_required('Inquiries')
def humanResources(request):
    context = {}
    return render(request, 'pages/human-resources.html', context)