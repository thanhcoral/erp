from django.urls import path

from apps.ts.views import humanResources


urlpatterns = [
    path('human-resources', humanResources, name='human-resources')
]