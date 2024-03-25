from django.urls import path

from recipe.views import ListCreateRecipesView, ReadUpdateDeleteRecipesView


urlpatterns = [
    path("recipes/", ListCreateRecipesView.as_view()),
    path("recipes/<int:pk>/", ReadUpdateDeleteRecipesView.as_view()),
]