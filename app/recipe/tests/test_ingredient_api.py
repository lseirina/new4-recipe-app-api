"""
Test for ingredients API.
"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Ingredient
from recipe.serializers import IngredientSerializer


INGREDIENT_URL = reverse('recipe:ingredient-list')


def create_user(email='test@example.com', password='test123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email=email, password=password)