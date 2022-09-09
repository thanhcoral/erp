from django.shortcuts import render


def humanResources(request):
    context = {}
    return render(request, 'pages/human-resources.html', context)