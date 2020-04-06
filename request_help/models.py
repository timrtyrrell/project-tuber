from django.db import models

LOCATIONS = (
    ('Clemons Library','Clemons Library'),
    ('Alderman Library', 'Alderman Library'),
    ('Clark Library','Clark Library'),
    ('Music Library','Music Library'),
    ('Rice Hall','Rice Hall'),
)


class HelpRequest(models.Model):
    class_name = models.CharField(max_length=20)
    topic = models.CharField(max_length=200)
    location = models.CharField(max_length=60, choices=LOCATIONS, default='green')
    # need to attach a user here for contact information

    def __str__(self):
        return self.topic