from django.db import models

from api.users import models as user_models


class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048, null=True, blank=True, default=None)
    notes = models.TextField(null=True, blank=True, default=None)

    created_by = models.ForeignKey(user_models.User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class RecipeIngredient(models.Model):
    id = models.BigAutoField(primary_key=True)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    quantity = models.DecimalField(max_digits=9, decimal_places=2)
    unit_of_measure = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    order = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class RecipeInstruction(models.Model):
    id = models.BigAutoField(primary_key=True)

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    text = models.CharField(max_length=256)
    order = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
