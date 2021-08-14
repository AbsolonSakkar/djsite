from django.contrib import admin
from django.contrib.auth import models
from django.contrib.auth.admin import UserAdmin

from main.models import User


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'name', 'is_staff')
    search_fields = ('username', 'name', 'email')
