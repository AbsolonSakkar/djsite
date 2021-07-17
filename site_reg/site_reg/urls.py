from django.contrib import admin

from main.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
    path('', include('main.urls')),  # http://127.0.0.1:8000/
]


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index),
#     path('register/', register),
#
# ]
