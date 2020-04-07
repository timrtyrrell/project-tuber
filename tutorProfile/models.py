from django.db import models

class TutorProfile(models.Model):
    class_name = models.CharField(max_length=40)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.class_name

        