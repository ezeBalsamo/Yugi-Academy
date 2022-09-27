from django.urls import path

from YuGiOh.cards.views import cards, find_or_store_spell_card

urlpatterns = [
    path('cards', cards, name="cards"),
    path('cards/registration', find_or_store_spell_card, name="find_or_store_spell_card"),
]
