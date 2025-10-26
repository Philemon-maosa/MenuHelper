from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.AllowAny]


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
def suggest_recipes(request):
    """
    Suggest recipes based on ingredients provided in query params.
    Example: /api/suggest/?ingredients=tomato,onion
    """
    ingredient_names = request.GET.get('ingredients', '').split(',')
    matching_recipes = set()

    for name in ingredient_names:
        name = name.strip().lower()
        if not name:
            continue
        recipes = Recipe.objects.filter(ingredients__name__icontains=name)
        matching_recipes.update(recipes)

    serializer = RecipeSerializer(list(matching_recipes), many=True)
    return Response(serializer.data)
