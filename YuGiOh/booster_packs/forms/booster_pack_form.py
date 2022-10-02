from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class BoosterPackForm(forms.Form):
    name = forms.CharField(label_suffix='', max_length=50)
    code = forms.CharField(label_suffix='', max_length=10)
    release_date = forms.DateField(label_suffix='', widget=DateInput)
