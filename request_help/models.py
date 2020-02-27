from django.db import models

class HelpRequest(models.Model):
    class_name = models.CharField(max_length=20)
    topic_text = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_text