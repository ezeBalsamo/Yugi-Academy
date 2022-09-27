from django.urls import path
from YuGiOh.booster_packs.views import booster_packs, find_or_store_booster_pack, \
    booster_pack_cards, find_or_store_booster_pack_card, delete_booster_pack_card

urlpatterns = [
    path('booster-packs', booster_packs, name="booster-packs"),
    path('booster-packs/registration', find_or_store_booster_pack, name="find_or_store_booster_pack"),
    path('booster-pack/<int:booster_pack_id>', booster_pack_cards, name="booster_pack"),
    path('booster-pack-cards/registration', find_or_store_booster_pack_card, name="find_or_store_booster_pack_card"),
    path('booster-pack-card/delete/<int:booster_pack_card_id>', delete_booster_pack_card, name="delete_booster_pack_card"),
]

