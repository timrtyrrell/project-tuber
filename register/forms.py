from django import forms
from .models import UserProfile


class PhoneForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)
    
    class Meta:
        model = UserProfile
        fields = ['name', 'phone']
