from django.db import models

# Create your models here.


class TutorStatus(models.Model):
    status = models.BooleanField()
    tutor = models.CharField(max_length=500)
    tutor_location = models.CharField(max_length=500)

