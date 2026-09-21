from django.shortcuts import render

from .models import Category, Skill


def home(request):
    categories = Category.objects.prefetch_related("skills").all()
    context = {
        "categories": categories,
        "skill_count": Skill.objects.count(),
        "category_count": categories.count(),
    }
    return render(request, "home.html", context)
