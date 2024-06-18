"""Tests for recipe API."""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework

from core.models import Recipe
from recipe.serialzers import RecipeSerializer

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