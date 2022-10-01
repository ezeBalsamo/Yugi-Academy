from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from YuGiOh.models import app
from assertions import SystemRestrictionInfringed


@login_required
def purge_trap_card(request, trap_card_id):
    trap_card = app.card_system.trap_card_numbered(trap_card_id)
    try:
        app.card_system.purge_trap_card(trap_card)
        messages.info(request, f'{trap_card} has been successfully deleted.')
    except SystemRestrictionInfringed as error:
        messages.error(request, str(error))
    return redirect('trap_cards')
