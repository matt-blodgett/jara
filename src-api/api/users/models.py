from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(null=False, max_length=30, unique=True)
    password = models.CharField(null=False, max_length=128)
    email = models.EmailField(null=False, max_length=128)
    first_name = models.CharField(null=True, max_length=45, default=None)
    last_name = models.CharField(null=True, max_length=45, default=None)
    is_active = models.BooleanField(null=False, default=True)
    dt_last_login = models.DateTimeField(null=True, default=None)
    dt_created = models.DateTimeField(null=False, auto_now_add=True)
    dt_modified = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        db_table = 'users'
