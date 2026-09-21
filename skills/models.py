from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify

            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="skills")

    class Meta:
        unique_together = ("category", "name")
        ordering = ["name"]

    def __str__(self):
        return self.name


class SkillLevel(models.Model):
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="skill_levels"
    )
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="levels")
    level = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )

    class Meta:
        unique_together = ("user", "skill")
        ordering = ["skill__category__name", "skill__name"]

    def __str__(self):
        return f"{self.user} — {self.skill} : {self.level}"
