from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BoosterPackForm(forms.Form):
    name = forms.CharField(max_length=50)
    code = forms.CharField(max_length=10)
    release_date = forms.DateField(widget=DateInput)
