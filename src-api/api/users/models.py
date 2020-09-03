from django.db import models

from api.library.models import JaraModel


class User(JaraModel):
    user_id = models.CharField(null=False, blank=False, max_length=45, unique=True)
    first_name = models.CharField(null=True, blank=False, max_length=45, default=None)
    last_name = models.CharField(null=True, blank=False, max_length=45, default=None)
    email = models.CharField(null=True, blank=False, max_length=128, default=None)
    password = models.CharField(null=True, blank=False, max_length=128)
    is_active = models.BooleanField(null=False, default=True)
    last_login_at = models.DateTimeField(null=True, default=None)
