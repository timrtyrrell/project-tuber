from django.forms import ModelForm, Select
from .models import HelpRequest
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class HelpRequestForm(ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['class_name', 'topic', 'location', 'time', 'day']
        widgets = {
            'location': Select(attrs={'class': 'form-control'}),
            'time': Select(attrs={'class': 'form-control'}),
            'day': DateInput()
        }
