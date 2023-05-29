import uuid
from django.db import models


class AccountModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
