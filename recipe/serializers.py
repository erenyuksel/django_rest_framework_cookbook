from rest_framework import serializers

from recipe.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'author', 'title', 'description', 'difficulty', 'created', 'updated', 'ingredients', "favorite"]

        class RecipeOnlySerializer(serializers.ModelSerializer):
            difficulty = serializers.CharField(source='get_difficulty_display')
            ingredients = serializers.CharField(source='get_ingredients_display')

            class Meta:
                model = Recipe
                fields = ['title', 'description', 'difficulty', 'created', 'updated', 'ingredients']

