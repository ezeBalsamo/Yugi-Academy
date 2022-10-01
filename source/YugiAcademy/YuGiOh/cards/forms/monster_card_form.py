from django import forms

from YuGiOh.cards import MonsterCard


class MonsterCardForm(forms.Form):
    name = forms.CharField(label_suffix='', max_length=50)
    race = forms.CharField(label_suffix='', max_length=25)
    attribute = forms.ChoiceField(label_suffix='', choices=MonsterCard.Attributes.choices)
    level = forms.IntegerField(label_suffix='', min_value=1, max_value=12)
    attack = forms.IntegerField(label_suffix='', min_value=0)
    defense = forms.IntegerField(label_suffix='', min_value=0)
    image = forms.ImageField(label_suffix='', required=False)
    description = forms.CharField(label_suffix='', max_length=8000, widget=forms.Textarea)
