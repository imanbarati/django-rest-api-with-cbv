from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreateAPIView(ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class RecipeRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

# uncomment below to avoid DRY
"""
# List view
class RecipeListView(ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

# Create view
class RecipeCreateView(CreateAPIView):
    serializer_class = RecipeSerializer

# Retrieve view
class RecipeRetrieveView(RetrieveAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

# Update view
class RecipeUpdateView(UpdateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

# Destroy view
class RecipeDeleteView(DestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
"""
