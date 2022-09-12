from django.urls import path

from apps.human_resources.views import human_resources, add_user, delete_user, edit_user


urlpatterns = [
    path('', human_resources, name='human-resources'),
    path('add-user', add_user, name='add-user'),
    path('edit-user/<int:pk>', edit_user, name='edit-user'),
    path('delete-user/<int:pk>', delete_user, name='delete-user'),
]