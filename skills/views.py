from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.mixins import AdminRequiredMixin, ManagerRequiredMixin
from accounts.models import User

from .forms import CategoryForm, SkillForm, SkillLevelForm
from .models import Category, Skill, SkillLevel


def _can_access_profile(viewer, target):
    if viewer == target:
        return True
    if viewer.is_admin_role:
        return True
    if viewer.is_manager_role and target.manager_id == viewer.id:
        return True
    return False


def _profile_redirect(pk, cat_id=None):
    url = reverse("profile_user", kwargs={"pk": pk})
    if cat_id:
        url += f"?cat={cat_id}"
    return redirect(url)


@login_required
def home(request):
    user = request.user
    context = {"user": user}
    if user.is_admin_role:
        context["categories_count"] = Category.objects.count()
        context["skills_count"] = Skill.objects.count()
        context["users_count"] = User.objects.count()
    if user.is_manager_role:
        context["employees"] = user.employees.all()
    return render(request, "dashboard.html", context)


@login_required
def profile(request, pk=None):
    target = request.user if pk is None else get_object_or_404(User, pk=pk)
    if not _can_access_profile(request.user, target):
        raise PermissionDenied

    can_edit = _can_access_profile(request.user, target)

    if request.method == "POST" and can_edit:
        action = request.POST.get("action", "set")
        skill = get_object_or_404(Skill, pk=request.POST.get("skill_id"))

        if action == "remove":
            SkillLevel.objects.filter(user=target, skill=skill).delete()
            messages.success(request, f"{skill.name} retirée du profil.")
            return _profile_redirect(target.pk, skill.category_id)

        form = SkillLevelForm(request.POST)
        if form.is_valid():
            level = form.cleaned_data["level"]
            if level >= 1:
                SkillLevel.objects.update_or_create(
                    user=target,
                    skill=skill,
                    defaults={"level": level},
                )
                messages.success(request, f"{skill.name} : niveau {level}/5.")
            else:
                SkillLevel.objects.filter(user=target, skill=skill).delete()
                messages.success(request, f"{skill.name} retirée du profil.")
        else:
            messages.error(request, "Niveau invalide (1 à 5 requis).")
        return _profile_redirect(target.pk, skill.category_id)

    selected_cat_id = None
    try:
        selected_cat_id = int(request.GET.get("cat"))
    except (TypeError, ValueError):
        selected_cat_id = None

    categories = Category.objects.prefetch_related("skills").all()
    selected = target.skill_levels.filter(level__gte=1).select_related("skill")

    selected_by_category = {}
    for sl in selected:
        selected_by_category.setdefault(sl.skill.category_id, []).append(
            (sl.skill, sl.level)
        )

    categories_data = []
    for category in categories:
        sel = sorted(selected_by_category.get(category.id, []), key=lambda x: x[0].name)
        sel_ids = {skill.id for skill, _ in sel}
        available = [s for s in category.skills.all() if s.id not in sel_ids]
        categories_data.append((category, sel, available))

    context = {
        "target": target,
        "can_edit": can_edit,
        "categories_data": categories_data,
        "selected_cat_id": selected_cat_id,
    }
    return render(request, "profile.html", context)


class EmployeeListView(ManagerRequiredMixin, ListView):
    model = User
    template_name = "employee_list.html"
    context_object_name = "employees"

    def get_queryset(self):
        qs = User.objects.filter(role=User.Role.USER)
        if self.request.user.is_manager_role:
            qs = qs.filter(manager=self.request.user)
        return qs.order_by("username")


class CategoryListView(AdminRequiredMixin, ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"


class CategoryCreateView(AdminRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "form.html"
    success_url = reverse_lazy("category_list")


class CategoryUpdateView(AdminRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "form.html"
    success_url = reverse_lazy("category_list")


class CategoryDeleteView(AdminRequiredMixin, DeleteView):
    model = Category
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("category_list")


class SkillListView(AdminRequiredMixin, ListView):
    model = Skill
    template_name = "skill_list.html"
    context_object_name = "skills"
    paginate_by = 50

    def get_queryset(self):
        return Skill.objects.select_related("category").order_by(
            "category__name", "name"
        )


class SkillCreateView(AdminRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = "form.html"
    success_url = reverse_lazy("skill_list")


class SkillUpdateView(AdminRequiredMixin, UpdateView):
    model = Skill
    form_class = SkillForm
    template_name = "form.html"
    success_url = reverse_lazy("skill_list")


class SkillDeleteView(AdminRequiredMixin, DeleteView):
    model = Skill
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("skill_list")
