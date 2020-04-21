from django import forms
from .models import UserProfile


class PhoneForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget= forms.TextInput
                           (attrs={'placeholder':'Your Name'}))
    phone = forms.CharField(max_length=10, widget= forms.TextInput
                           (attrs={'placeholder':'XXXXXXXXXX'}))
    
    class Meta:
        model = UserProfile
        fields = ['name', 'phone']


class TutorProfileForm(forms.Form): 
    class_name = forms.CharField(max_length = 40, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter class name', 'aria-label': 'Class', 'aria-describedby' : 'add-btn'
}
        )
    )