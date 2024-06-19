"""Serializers for recipe APIs."""
from rest_faramework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.Serializer):
    """Serializer for recipes."""
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
