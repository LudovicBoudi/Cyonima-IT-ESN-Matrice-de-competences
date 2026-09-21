from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role", "manager")
    list_filter = ("role", "manager")
    fieldsets = UserAdmin.fieldsets + (
        ("GPEC", {"fields": ("role", "manager")}),
    )
