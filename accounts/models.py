from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Administrateur"
        MANAGER = "manager", "Manager"
        USER = "user", "Utilisateur"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.USER)
    manager = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="employees",
        limit_choices_to={"role": Role.MANAGER},
    )

    @property
    def is_admin_role(self):
        return self.role == self.Role.ADMIN

    @property
    def is_manager_role(self):
        return self.role == self.Role.MANAGER

    def __str__(self):
        return self.get_full_name() or self.username
