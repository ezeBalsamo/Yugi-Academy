from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from YuGiOh.models import app


@login_required
def spell_cards(request):
    context = {
        'card_type': 'spell',
        'store_url': 'store_spell_card',
        'update_url': 'update_spell_card',
        'purge_url': 'purge_spell_card',
        'cards': app.card_system.spell_cards()
    }
    return render(request, "YuGiOh/cards.html", context)
