from django.shortcuts import redirect

from YuGiOh.models import booster_pack_system


def delete_booster_pack_card(request, booster_pack_card_id: int):
    booster_pack_card = booster_pack_system().booster_pack_card_numbered(booster_pack_card_id)
    booster_pack_system().purge_booster_pack_card(booster_pack_card)
    return redirect(f'/yugioh/booster-pack/{booster_pack_card.booster_pack.id}')
