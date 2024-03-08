from django.db import models
from django.contrib.auth.models import User

# Model subscribers
class SenderModel(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    subscribe = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name