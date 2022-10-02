from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from YuGiOh.models import app


@login_required
def trap_cards(request):
    context = {
        'card_type': 'trap',
        'store_url': 'store_trap_card',
        'update_url': 'update_trap_card',
        'purge_url': 'purge_trap_card',
        'cards': app.card_system.trap_cards()
    }
    return render(request, "YuGiOh/cards.html", context)
