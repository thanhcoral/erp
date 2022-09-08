from django.urls import path
from django.contrib.auth import views as auth_views

from apps.authentication.views import login_view, register_view


urlpatterns = [
    # path('login', login_view, name='login'),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='logout'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('change-password', auth_views.PasswordChangeView.as_view(success_url='change-password-done'), name='change-password'),
    path('change-password-done', auth_views.PasswordChangeDoneView.as_view(), name='change-password-done'),
    path('register', register_view, name='register'),
]