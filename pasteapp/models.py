import uuid
from django.db import models


class Paste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    language = models.CharField(max_length=32)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=1)
