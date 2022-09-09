from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required("user.view_user", raise_exception=True)
def humanResources(request):
    context = {}
    return render(request, 'pages/human-resources.html', context)