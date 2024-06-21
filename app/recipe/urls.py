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
router

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]