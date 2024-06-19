"""
Urls mapping for the redipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

url_patterns = [
    path('', include(router.urls))
]