from models import *
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient


class IngredientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientCategory


class MeasurementSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = Measurement


class RecipeSerializer(serializers.ModelSerializer):
    measurement_set = MeasurementSerializer(many=True)

    class Meta:
        model = Recipe


