from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from YuGiOh.models import app
from assertions import SystemRestrictionInfringed


@login_required
def purge_monster_card(request, monster_card_id):
    monster_card = app.card_system.monster_card_numbered(monster_card_id)
    try:
        app.card_system.purge_monster_card(monster_card)
        messages.info(request, f'{monster_card} has been successfully deleted.')
    except SystemRestrictionInfringed as error:
        messages.error(request, str(error))
    return redirect('monster_cards')
