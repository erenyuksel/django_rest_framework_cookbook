from django.contrib import admin
from .models import Cookbook
class CookbookAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'description')

admin.site.register(Cookbook, CookbookAdmin)
