from django.shortcuts import render
from rest_framework import generics
from serializers import *
# Create your views here.


class RecipeList(generics.ListCreateAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Recipe
    serializer_class = RecipeSerializer


class IngredientList(generics.ListAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer