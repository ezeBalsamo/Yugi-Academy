from django import forms


class BoosterPackForm(forms.Form):
    name = forms.CharField(max_length=50)
    code = forms.CharField(max_length=10)
    release_date = forms.DateField()
