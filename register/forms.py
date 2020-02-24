from django import forms
from .models import UserProfile


class PhoneForm(forms.ModelForm):
    phone = forms.CharField(max_length=10)

    class Meta:
        model = UserProfile
        fields = ('phone',)