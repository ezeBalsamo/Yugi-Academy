from django.urls import path

from YuGiOh.cards.views import cards, store_spell_card

urlpatterns = [
    path('cards', cards, name="cards"),
    path('cards/registration', store_spell_card, name="store_spell_card"),
]
