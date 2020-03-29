from django import forms

CHOICES = [('Yes','Yes'),
         ('No','No')]

LOCATIONS = (
    ('clem','Clemons Library'),
    ('aldy', 'Alderman Library'),
    ('clark','Clark Library'),
    ('music','Music Library'),
    ('rice','Rice Hall'),
)

class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    location = forms.ChoiceField(choices=LOCATIONS, widget=forms.Select(attrs={'class': 'form-control'}))

    