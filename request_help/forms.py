from django.forms import ModelForm, Select
from .models import HelpRequest

class HelpRequestForm(ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['class_name', 'topic', 'location']
        widgets = {
            'location': Select(attrs={'class': 'form-control'}),
        }
    