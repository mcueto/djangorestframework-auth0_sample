from django.conf import settings
from django.db import models

class ToDo(models.Model):
    text = models.TextField()
    done = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.text
