from models import *
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient


class IngredientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientCategory


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe