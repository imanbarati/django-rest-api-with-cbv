# models.py
from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

