from django.db import models
from django.contrib.auth.models import User

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    status = models.BooleanField(choices=BOOL_CHOICES, default=False)
    status_string = models.CharField(max_length=30, default="Not Available")
    tutor_location = models.CharField(max_length=20, default="Anywhere")
