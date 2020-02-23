from django.db import models

class HelpRequest(models.Model):
    class_name = models.CharField(max_length=20)
    topic_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.topic_text