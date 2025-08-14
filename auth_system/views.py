from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from auth_system.forms import LoginForm, RegisterForm

class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = LoginForm

class RegisterView(CreateView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy('login')