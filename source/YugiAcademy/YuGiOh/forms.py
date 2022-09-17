from django import forms
from cards.spell_card import SpellCard
from booster_packs.booster_pack import BoosterPack


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


class BoosterPackCardForm(forms.Form):
    card = forms.ModelChoiceField(SpellCard.objects.all())
    booster_pack = forms.ModelChoiceField(BoosterPack.objects.all())
    identifier = forms.CharField(max_length=20)
    rarity = forms.CharField(max_length=20)
