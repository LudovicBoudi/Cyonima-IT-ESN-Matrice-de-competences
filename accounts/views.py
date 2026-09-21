from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UserCreateForm, UserEditForm
from .mixins import AdminRequiredMixin
from .models import User


class UserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = "accounts/user_list.html"
    context_object_name = "users"
    ordering = ["username"]


class UserCreateView(AdminRequiredMixin, CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        messages.success(self.request, "Utilisateur créé.")
        return super().form_valid(form)


class UserUpdateView(AdminRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "form.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        messages.success(self.request, "Utilisateur mis à jour.")
        return super().form_valid(form)


class UserDeleteView(AdminRequiredMixin, DeleteView):
    model = User
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        messages.success(self.request, "Utilisateur supprimé.")
        return super().form_valid(form)


class AssignEmployeesView(LoginRequiredMixin, ListView):
    template_name = "accounts/assign_employees.html"
    context_object_name = "users"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_manager_role:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return User.objects.filter(
            role=User.Role.USER, manager__isnull=True
        ).order_by("username")

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.POST.get("user_id"))
        if user.role != User.Role.USER:
            messages.error(request, "Seuls les utilisateurs peuvent être assignés.")
        else:
            user.manager = request.user
            user.save(update_fields=["manager"])
            messages.success(request, f"{user} est maintenant votre collaborateur.")
        return redirect("assign_employees")
