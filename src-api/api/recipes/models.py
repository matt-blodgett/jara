from django.db import models

from api.library.models import JaraModel


class Recipe(JaraModel):
    created_by = models.CharField(null=False, blank=False, max_length=45)
    guid = models.CharField(null=False, blank=False, max_length=128)
    title = models.CharField(null=False, blank=False, max_length=45)
    description = models.TextField(null=True, blank=False, default=None)


class Instruction(JaraModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    index = models.IntegerField(null=False)
    text = models.TextField(null=False, blank=False)


class Ingredient(JaraModel):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    index = models.IntegerField(null=False)
    text = models.TextField(null=False, blank=False)
