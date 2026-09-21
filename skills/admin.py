from django.contrib import admin

from .models import Category, Skill, SkillLevel


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "skill_count")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SkillInline]

    @admin.display(description="Compétences")
    def skill_count(self, obj):
        return obj.skills.count()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(SkillLevel)
class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ("user", "skill", "level")
    list_filter = ("level", "skill__category")
    search_fields = ("user__username", "skill__name")
