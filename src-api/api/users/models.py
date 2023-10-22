from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(null=False, max_length=30, unique=True)
    password = models.CharField(null=False, max_length=128)
    email = models.EmailField(null=False, max_length=128, unique=True)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    modified_at = models.DateTimeField(null=False, auto_now=True)
