from django.db import models
from django.utils import timezone
import sys
from register.models import UserProfile

LOCATIONS = (
    ('Clemons Library','Clemons Library'),
    ('Alderman Library', 'Alderman Library'),
    ('Clark Library','Clark Library'),
    ('Music Library','Music Library'),
    ('Rice Hall','Rice Hall'),
)

TIMES = (
    (5,'5 Minutes'),
    (10, '10 Minutes'),
    (15,'15 Minutes'),
    (30,'30 Minutes'),
    (60,'1 Hour'),
)

class HelpRequest(models.Model):
    class_name = models.CharField(max_length=20)
    topic = models.CharField(max_length=200)
    location = models.CharField(max_length=60, choices=LOCATIONS, default='green')
    time = models.IntegerField(choices=TIMES, default=5)
    day = models.DateField(max_length=100,default = timezone.now)
    # need to attach a user here for contact information
    name = models.CharField(max_length=60, default='Not Real Name')
    phone = models.CharField(max_length=60, default='XXXXXXXXXX')
    user = UserProfile()

    def __str__(self):
        return self.topic