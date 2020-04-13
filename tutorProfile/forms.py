from django import forms

class CreateNewList(forms.Form):
    major = forms.CharField(label="Major",max_length=100)
    course = forms.CharField(label="Course Name",max_length=200)
    check = forms.BooleanField(label="Taken?",required=False)
                            
