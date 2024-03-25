from django.db import models
from user.models import User
from recipe.models import Recipe
from django.contrib.auth.models import User


class Cookbook(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
