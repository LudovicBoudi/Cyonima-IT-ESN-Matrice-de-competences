from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Category, Skill, SkillLevel


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ["name", "category"]


class SkillLevelForm(forms.ModelForm):
    level = forms.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        widget=forms.RadioSelect(choices=[(i, str(i)) for i in range(0, 6)]),
    )

    class Meta:
        model = SkillLevel
        fields = ["level"]
