from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


from .views import RegisterView, custom_logout_view, profile, ResetPasswordView, signupuser, loginuser, logoutuser, \
    ResetPasswordConfirmView

app_name = 'app_users'

urlpatterns = [
    path('signup/', signupuser, name='signup'),
    path('login/', loginuser, name='login'),
    path('logout/', logoutuser, name='logout'),
    path('profile/', profile, name='profile'),
    path('reset-password/', ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='app_users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='app_users/password_reset_confirm.html',
        success_url=reverse_lazy('/app_users/password_reset_complete/')), name='password_reset_confirm'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='app_users/password_reset_complete.html'),
         name='password_reset_complete'),
]

