from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='+')
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)