from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from YuGiOh.models import app
from assertions import SystemRestrictionInfringed


@login_required
def purge_spell_card(request, spell_card_id):
    spell_card = app.card_system.spell_card_numbered(spell_card_id)
    try:
        app.card_system.purge_spell_card(spell_card)
        messages.info(request, f'{spell_card} has been successfully deleted.')
    except SystemRestrictionInfringed as error:
        messages.error(request, str(error))
    return redirect('spell_cards')
