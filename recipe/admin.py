from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", 'title', 'author', 'created', 'updated')
    list_filter = ('author', 'created', 'updated')
    search_fields = ('title', 'description')
admin.site.register(Recipe, RecipeAdmin)
