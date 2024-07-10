from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .views import RegisterView, custom_logout_view

app_name = 'app_users'

urlpatterns = [
    path("register/", RegisterView.as_view(), name='register'),
    path("login/", auth_views.LoginView.as_view(template_name='app_users/login.html'), name='login'),
    path("logout/", custom_logout_view, name='logout'),
]
