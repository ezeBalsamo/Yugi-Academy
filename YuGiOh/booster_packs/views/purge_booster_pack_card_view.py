from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from YuGiOh.models import app
from assertions import SystemRestrictionInfringed


@login_required
def purge_booster_pack_card(request, booster_pack_card_id: int):
    booster_pack_card = app.booster_pack_system.booster_pack_card_numbered(booster_pack_card_id)
    booster_pack = booster_pack_card.booster_pack
    try:
        app.booster_pack_system.purge_booster_pack_card(booster_pack_card)
        messages.info(request, f'{booster_pack_card} has been successfully deleted.')
    except SystemRestrictionInfringed as error:
        messages.error(request, str(error))
    return redirect(f'/yugioh/booster-pack-cards/booster-pack/{booster_pack.id}')