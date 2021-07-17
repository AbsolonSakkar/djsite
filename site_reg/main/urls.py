from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),  # http://127.0.0.1:8000/
    path('register/', RegisterUser.as_view(), name='register'),  # http://127.0.0.1:8000/register/
    path('login/', login, name='login'),  # http://127.0.0.1:8000/login/
]

