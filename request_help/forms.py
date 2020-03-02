from django.forms import ModelForm, TextInput
from .models import HelpRequest

class HelpRequestForm(ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['class_name', 'topic_text', 'location']