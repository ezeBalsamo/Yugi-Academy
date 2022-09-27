from django.shortcuts import render
from YuGiOh.models import app


def booster_pack_cards(request, booster_pack_id: id):
    booster_pack = app.booster_pack_system.booster_pack_numbered(booster_pack_id)

    context = {
        'booster_pack': booster_pack,
        'booster_pack_cards': app.booster_pack_system.booster_pack_cards_in(booster_pack)
    }
    return render(request, "YuGiOh/booster_pack_cards.html", context)
