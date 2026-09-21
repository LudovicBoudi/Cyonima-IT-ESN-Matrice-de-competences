from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserFormMixin(forms.ModelForm):
    manager = forms.ModelChoiceField(
        queryset=User.objects.filter(role=User.Role.MANAGER),
        required=False,
        label="Manager",
    )


class UserCreateForm(UserFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "manager",
        )


class UserEditForm(UserFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "manager",
            "is_active",
        )
