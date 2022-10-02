from django import forms


class SearchBoosterPackForm(forms.Form):
    name = forms.CharField(max_length=50, label="")

    def __str__(self):
        return 'Form for searching booster packs through their name'
