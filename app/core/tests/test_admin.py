"""
Tests for admin modification
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTest(TestCase):
    """Test user list."""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            'admin@example.com',
            'test123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='test123',
            name='Test User',
        )

    def test_users_list(self):
        """Test that users listed on page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)
