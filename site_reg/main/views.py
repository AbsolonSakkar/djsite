from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import RegisterUserForm


def index(request):
    return render(request, 'main/index.html',
                  {'enter': 'Войти в аккаунт', 'reg_user': 'Зарегистрироваться', 'index_title': 'Добро пожаловать!'})


def register(request):
    return render(request, 'main/reg.html', {'reg_title': 'Регистрация'})


def login(request):
    return render(request, 'main/login.html', {'login_title': 'Вход'})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('login')
