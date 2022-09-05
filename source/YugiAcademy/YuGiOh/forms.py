from django import forms


class SpellCardForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=8000)
    type = forms.CharField(max_length=20)


class SearchBoosterPackForm(forms.Form):
    name = forms.CharField(max_length=50)

    def __str__(self):
        return 'Form for searching booster packs through their name'


class BoosterPackForm(forms.Form):
    name = forms.CharField(max_length=50)
    code = forms.CharField(max_length=10)
    release_date = forms.DateField()
