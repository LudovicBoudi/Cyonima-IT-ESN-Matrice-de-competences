from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("profile/<int:pk>/", views.profile, name="profile_user"),
    path("employees/", views.EmployeeListView.as_view(), name="employee_list"),
    path(
        "categories/", views.CategoryListView.as_view(), name="category_list"
    ),
    path(
        "categories/create/",
        views.CategoryCreateView.as_view(),
        name="category_create",
    ),
    path(
        "categories/<int:pk>/edit/",
        views.CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/<int:pk>/delete/",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("skills/", views.SkillListView.as_view(), name="skill_list"),
    path("skills/create/", views.SkillCreateView.as_view(), name="skill_create"),
    path(
        "skills/<int:pk>/edit/", views.SkillUpdateView.as_view(), name="skill_update"
    ),
    path(
        "skills/<int:pk>/delete/",
        views.SkillDeleteView.as_view(),
        name="skill_delete",
    ),
]
