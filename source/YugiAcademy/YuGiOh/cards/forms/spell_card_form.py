from django import forms

from YuGiOh.cards import SpellCard


class SpellCardForm(forms.Form):
    name = forms.CharField(label_suffix='', max_length=50)
    type = forms.ChoiceField(label_suffix='', choices=SpellCard.Types.choices)
    image = forms.ImageField(label_suffix='', required=False)
    description = forms.CharField(label_suffix='', max_length=8000, widget=forms.Textarea)
