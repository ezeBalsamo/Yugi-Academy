from django import forms

from YuGiOh.cards import SpellCard
from YuGiOh.booster_packs import BoosterPack


class BoosterPackCardForm(forms.Form):
    card = forms.ModelChoiceField(SpellCard.objects.all())
    booster_pack = forms.ModelChoiceField(BoosterPack.objects.all())
    identifier = forms.CharField(max_length=20)
    rarity = forms.CharField(max_length=20)
