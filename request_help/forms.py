from django.forms import ModelForm
from .models import HelpRequest

class HelpRequestForm(ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['class_name', 'topic', 'location']