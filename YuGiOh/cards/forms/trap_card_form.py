from django import forms

from YuGiOh.cards import TrapCard


class TrapCardForm(forms.Form):
    name = forms.CharField(label_suffix='', max_length=50)
    type = forms.ChoiceField(label_suffix='', choices=TrapCard.Types.choices)
    image = forms.ImageField(label_suffix='', required=False)
    description = forms.CharField(label_suffix='', max_length=8000, widget=forms.Textarea)
