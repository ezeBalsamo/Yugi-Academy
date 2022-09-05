from django import forms


class SpellCardForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=8000)
    type = forms.CharField(max_length=20)
