from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from YuGiOh.models import app
from YuGiOh.booster_packs import BoosterPackCard


@login_required
def booster_pack_cards(request, booster_pack_id: id):
    booster_pack = app.booster_pack_system.booster_pack_numbered(booster_pack_id)

    context = {
        'booster_pack': booster_pack,
        'store_url': 'store_booster_pack_card',
        'update_url': 'update_booster_pack_card',
        'purge_url': 'purge_booster_pack_card',
        'type_description': BoosterPackCard.type_description,
        'booster_pack_cards': app.booster_pack_system.booster_pack_cards_in(booster_pack)
    }
    return render(request, "YuGiOh/booster_pack_cards.html", context)
