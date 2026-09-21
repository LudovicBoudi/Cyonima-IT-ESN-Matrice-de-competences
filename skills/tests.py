from django.test import TestCase
from django.urls import reverse

from accounts.models import User
from .models import Category, Skill, SkillLevel


class PermissionTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username="admin", password="x", role=User.Role.ADMIN)
        self.manager = User.objects.create_user(username="manager", password="x", role=User.Role.MANAGER)
        self.employee = User.objects.create_user(
            username="employee", password="x", role=User.Role.USER, manager=self.manager
        )
        self.other = User.objects.create_user(username="other", password="x", role=User.Role.USER)

    def test_user_can_view_own_profile(self):
        self.client.login(username="employee", password="x")
        resp = self.client.get(reverse("profile"))
        self.assertEqual(resp.status_code, 200)

    def test_user_cannot_view_other_profile(self):
        self.client.login(username="other", password="x")
        resp = self.client.get(reverse("profile_user", args=[self.employee.pk]))
        self.assertEqual(resp.status_code, 403)

    def test_manager_can_view_employee(self):
        self.client.login(username="manager", password="x")
        resp = self.client.get(reverse("profile_user", args=[self.employee.pk]))
        self.assertEqual(resp.status_code, 200)

    def test_manager_cannot_view_non_employee(self):
        self.client.login(username="manager", password="x")
        resp = self.client.get(reverse("profile_user", args=[self.other.pk]))
        self.assertEqual(resp.status_code, 403)

    def test_admin_can_view_any_profile(self):
        self.client.login(username="admin", password="x")
        resp = self.client.get(reverse("profile_user", args=[self.employee.pk]))
        self.assertEqual(resp.status_code, 200)

    def test_non_admin_cannot_manage_categories(self):
        self.client.login(username="manager", password="x")
        resp = self.client.get(reverse("category_list"))
        self.assertEqual(resp.status_code, 403)


class SkillLevelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", password="x", role=User.Role.USER)
        self.category = Category.objects.create(name="Test", slug="test")
        self.skill = Skill.objects.create(name="Python", category=self.category)

    def test_set_level_updates(self):
        self.client.login(username="u", password="x")
        resp = self.client.post(
            reverse("profile"),
            {"skill_id": self.skill.pk, "level": "4"},
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(SkillLevel.objects.get(user=self.user, skill=self.skill).level, 4)

    def test_level_above_5_rejected(self):
        self.client.login(username="u", password="x")
        self.client.post(reverse("profile"), {"skill_id": self.skill.pk, "level": "6"})
        self.assertFalse(SkillLevel.objects.filter(user=self.user, skill=self.skill).exists())
