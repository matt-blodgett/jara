import datetime

from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(null=False, max_length=45, blank=False, unique=True)
    first_name = models.CharField(null=True, max_length=45, blank=False, default=None)
    last_name = models.CharField(null=True, max_length=45, blank=False, default=None)
    email = models.CharField(null=True, max_length=128, blank=False, default=None)
    password = models.CharField(null=True, max_length=128, blank=False)
    is_active = models.BooleanField(null=False, default=True)
    dt_last_login = models.DateTimeField(null=True, default=None)
    dt_created = models.DateTimeField(null=False)
    dt_modified = models.DateTimeField(null=False)

    def save(self, **kwargs):
        self.dt_modified = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        super().save(**kwargs)

    class Meta:
        db_table = 'users'
