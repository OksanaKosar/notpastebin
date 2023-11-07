from django.contrib.auth import logout, login

from django.contrib.auth.views import LoginView

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user_management.forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "user_management/register.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):

    form_class = LoginUserForm
    template_name = 'user_management/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
