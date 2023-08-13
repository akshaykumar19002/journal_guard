from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    hash_salt = models.CharField(max_length=128, blank=True, null=True)
    encryption_required = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username
