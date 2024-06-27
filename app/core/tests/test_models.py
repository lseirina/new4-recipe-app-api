"""
Tests for models
"""
from unittest.mock import patch

from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user():
    """Create and return user."""
    return get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123'
    )


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_success(self):
        """Test creating user model."""
        email = 'test@example.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test normalization user email"""
        sample_emails = [
            ['test1@example.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com']
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'testpass123')
            self.assertEqual(user.email, expected)

    def test_creating_new_user_without_email_raises_error(self):
        """Test that creating a new user without email raises ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testpass123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'testpass123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating recipe is successfull."""
        user = create_user()
        recipe = models.Recipe.objects.create(
            user=user,
            title='New Recipe',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description.'
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a tag is successful."""
        user = create_user()
        tag = models.Tag.objects.create(
            user=user,
            name='tag1'
        )

        self.assertEqual(str(tag), tag.name)

    def test_create_ingredients(self):
        """Test creating ingredients is successful."""
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            name='Flour',
            user=user,
        )

        self.assertEqual(str(ingredient), ingredient.name)

    @patch('core.models.uuid.uuid4')
    def test_create_path_upload_image(self, mock_uuid):
        """Test creating path for uploading images."""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        path = models.recipe_image_file_path(None, 'example.jpg')
        self.assertEqual(path, f'uploads/recipe/{uuid}.jpg')