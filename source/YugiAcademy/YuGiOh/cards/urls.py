from django.urls import path

from YuGiOh.cards.views import spell_cards, store_spell_card

urlpatterns = [
    path('spell-cards', spell_cards, name="spell_cards"),
    path('spell-card/registration', store_spell_card, name="store_spell_card"),
]
