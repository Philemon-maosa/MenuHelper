from rest_framework import generics
from .models import Ingredient
from .serializers import IngredientSerializer

# List all ingredients / Add new ingredient
class IngredientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

# Retrieve, Update, Delete ingredient by ID
class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
