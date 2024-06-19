"""Tests for recipe API."""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Recipe
from recipe.serialzers import RecipeSerializer

RECIPE_URL = reverse('recipe:recipe-list')

def create_recipe(user, **params):
    """Create and return recipe."""
    defaults = {
        'title': 'New Recipe',
        'time_minutes': 22,
        'price': Decimal('3.50'),
        'description': 'Sample description',
        'link': 'http://example.com/recipe.pdf',
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)

    return recipe


class PublicRecipeAPITests(TestCase):
    """Test unauthenticated API requests."""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test uthentication required ror requests."""
        res = self.client.get(RECIPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
