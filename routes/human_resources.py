from django.urls import path

from apps.human_resources.views import human_resources, add_user


urlpatterns = [
    path('', human_resources, name='human-resources'),
    path('add-user', add_user, name='add-user'),
]