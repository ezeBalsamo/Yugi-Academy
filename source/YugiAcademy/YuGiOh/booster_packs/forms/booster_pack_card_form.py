from django import forms

from YuGiOh.models import app


def all_cards_as_list_of_tuple():
    cards = app.card_system.spell_cards() + app.card_system.trap_cards() + app.card_system.monster_cards()
    return [(card, card) for card in cards]


class BoosterPackCardForm(forms.Form):
    card = forms.ChoiceField(label_suffix='', choices=all_cards_as_list_of_tuple())
    booster_pack = forms.CharField(label_suffix='', disabled=True, required=False)
    identifier = forms.CharField(label_suffix='', max_length=20)
    rarity = forms.CharField(label_suffix='', max_length=20)
