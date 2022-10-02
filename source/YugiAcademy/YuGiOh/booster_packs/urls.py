from django.urls import path
from YuGiOh.booster_packs.views import booster_packs, store_booster_pack, update_booster_pack, purge_booster_pack, \
    booster_pack_cards, store_booster_pack_card, update_booster_pack_card, purge_booster_pack_card

urlpatterns = [
    path('booster-packs', booster_packs, name="booster_packs"),
    path('booster-pack/registration', store_booster_pack, name="store_booster_pack"),
    path('booster-pack/update/<int:booster_pack_id>', update_booster_pack, name="update_booster_pack"),
    path('booster-pack/purge/<int:booster_pack_id>', purge_booster_pack, name="purge_booster_pack"),

    path('booster-pack-cards/booster-pack/<int:booster_pack_id>', booster_pack_cards, name="booster_pack_cards"),
    path('booster-pack-cards/booster-pack/<int:booster_pack_id>/registration', store_booster_pack_card,
         name="store_booster_pack_card"),
    path('booster-pack-cards/booster-pack/update/<int:booster_pack_card_id>',
         update_booster_pack_card,
         name="update_booster_pack_card"),
    path('booster-pack-card/purge/<int:booster_pack_card_id>', purge_booster_pack_card, name="purge_booster_pack_card"),
]
