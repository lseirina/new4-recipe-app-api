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


class PublicIngredientsAPITests(TestCase):
    """Tests unauthenticated API requests."""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required for retrieving ingredients."""
        res = self.client.get(INGREDIENT_URL)

        self.assertequal(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivatIngredientAPITest(TestCase):
    """Tests authenticated API requests."""
    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_ingredients(self):
        """Test retrieving a list of ingredients."""
        Ingredient.objects.create(
            user=self.user,
            name='Salt',
        )
        Ingredient.objects.create(
            user=self.user,
            name='Sugar',
        )
        res = self.client.get(INGREDIENT_URL)

        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_ingrdients_limited_to_user(self):
        """Test ingredients limited to authenticated user."""
        new_user = get_user_model().objects.create_user(
            email='user1@example.com',
            password='test123',
        )
        Ingredient.objects.create(user=new_user, name='Apples')
        ingredient = Ingredient.objects.create(user=self.user, name='Kivi')

        res = self.client.get(INGREDIENT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertequal(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], ingredient.name)
        self.assertEqual(res.data[0]['id'], ingredient.id)
