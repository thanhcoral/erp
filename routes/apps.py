from django.urls import path

from apps.hello.views import home


urlpatterns = [
    path('home', home, name='home')
]