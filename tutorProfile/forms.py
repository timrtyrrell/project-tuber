from django import forms

class TutorProfileForm(forms.Form): 
    class_name = forms.CharField(max_length = 40, 
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter class name', 'aria-label': 'Class', 'aria-describedby' : 'add-btn'
}
        )
    )