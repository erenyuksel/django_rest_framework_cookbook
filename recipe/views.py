from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from recipe.models import Recipe
from recipe.serializers import RecipeSerializer


class ListCreateRecipesView(GenericAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return Recipe.objects.all()

    def get(self, request, *args, **kwargs):
        recipes = self.get_queryset()
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

     serializer = self.get_serializer(data=request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     return Response(serializer.data)

class ReadUpdateDeleteRecipesView(GenericAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)