from django.test import TestCase
from django.urls import reverse

from .models import User


class AssignEmployeesTests(TestCase):
    def setUp(self):
        self.manager = User.objects.create_user(username="manager", password="x", role=User.Role.MANAGER)
        self.manager2 = User.objects.create_user(username="manager2", password="x", role=User.Role.MANAGER)
        self.admin = User.objects.create_user(username="admin", password="x", role=User.Role.ADMIN)
        self.free = User.objects.create_user(username="free", password="x", role=User.Role.USER)

    def test_manager_can_assign_free_user(self):
        self.client.login(username="manager", password="x")
        resp = self.client.post(reverse("assign_employees"), {"user_id": self.free.pk})
        self.assertEqual(resp.status_code, 302)
        self.free.refresh_from_db()
        self.assertEqual(self.free.manager, self.manager)

    def test_assign_page_lists_only_unassigned(self):
        assigned = User.objects.create_user(username="assigned", password="x", role=User.Role.USER, manager=self.manager)
        self.client.login(username="manager2", password="x")
        resp = self.client.get(reverse("assign_employees"))
        self.assertContains(resp, "free")
        self.assertNotContains(resp, assigned.username)

    def test_user_cannot_access_assign_page(self):
        self.client.login(username="free", password="x")
        resp = self.client.get(reverse("assign_employees"))
        self.assertEqual(resp.status_code, 403)

    def test_admin_cannot_access_assign_page(self):
        self.client.login(username="admin", password="x")
        resp = self.client.get(reverse("assign_employees"))
        self.assertEqual(resp.status_code, 403)
