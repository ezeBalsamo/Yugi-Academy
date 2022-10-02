from django.urls import path

from YuGiOh.cards.views import spell_cards, store_spell_card, update_spell_card, purge_spell_card, \
                                trap_cards, store_trap_card, update_trap_card, purge_trap_card, \
                                monster_cards, store_monster_card, update_monster_card, purge_monster_card

urlpatterns = [
    path('spell-cards', spell_cards, name="spell_cards"),
    path('spell-card/registration', store_spell_card, name="store_spell_card"),
    path('spell-card/update/<int:spell_card_id>', update_spell_card, name="update_spell_card"),
    path('spell-card/purge/<int:spell_card_id>', purge_spell_card, name="purge_spell_card"),

    path('trap-cards', trap_cards, name="trap_cards"),
    path('trap-card/registration', store_trap_card, name="store_trap_card"),
    path('trap-card/update/<int:trap_card_id>', update_trap_card, name="update_trap_card"),
    path('trap-card/purge/<int:trap_card_id>', purge_trap_card, name="purge_trap_card"),

    path('monster-cards', monster_cards, name="monster_cards"),
    path('monster-card/registration', store_monster_card, name="store_monster_card"),
    path('monster-card/update/<int:monster_card_id>', update_monster_card, name="update_monster_card"),
    path('monster-card/purge/<int:monster_card_id>', purge_monster_card, name="purge_monster_card"),
]
