from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from YuGiOh.models import app
from assertions import SystemRestrictionInfringed


@login_required
def purge_booster_pack(request, booster_pack_id):
    booster_pack = app.booster_pack_system.booster_pack_numbered(booster_pack_id)
    try:
        app.booster_pack_system.purge_booster_pack(booster_pack)
    except SystemRestrictionInfringed as error:
        messages.error(request, str(error))
    return redirect('/yugioh/booster-packs')
