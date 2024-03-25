from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(blank=True,    max_length=255)
    description = models.TextField()
    ingredients = models.TextField(blank=True, null=True)
    favorite = models.BooleanField(default=False)
    difficulty = models.IntegerField(choices=[
        (1, 'Easy'),
        (2, 'Intermediate'),
        (3, 'Hard'),
    ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, related_name='recipes', on_delete=models.CASCADE)

