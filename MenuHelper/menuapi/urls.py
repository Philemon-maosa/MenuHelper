from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IngredientViewSet, RecipeViewSet, suggest_recipes

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'recipes', RecipeViewSet, basename='recipe')

# Define all URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Ingredients & Recipes API endpoints
    path('suggest/', suggest_recipes, name='suggest_recipes'),  # Recipe suggestion endpoint
]
