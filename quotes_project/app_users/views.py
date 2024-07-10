from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm

class RegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'app_users/register.html'
    success_url = reverse_lazy('app_quotes:home')


def custom_logout_view(request):
    logout(request)
    return redirect('app_quotes:home')