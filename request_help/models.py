from django.db import models

LOCATIONS = (
    ('clem','Clemons Library'),
    ('aldy', 'Alderman Library'),
    ('clark','Clark Library'),
    ('music','Music Library'),
    ('rice','Rice Hall'),
)


class HelpRequest(models.Model):
    class_name = models.CharField(max_length=20)
    topic = models.CharField(max_length=200)
    location = models.CharField(max_length=6, choices=LOCATIONS, default='green')
    # need to attach a user here for contact information

    def __str__(self):
        return self.topic