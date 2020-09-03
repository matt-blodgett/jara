import datetime

from django.db import models


class JaraModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(null=False)
    modified_at = models.DateTimeField(null=False)

    def save(self, **kwargs):
        self.modified_at = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        super().save(**kwargs)

    class Meta:
        abstract = True
