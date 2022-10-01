from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from YuGiOh.models import app


@login_required
def monster_cards(request):
    context = {
        'card_type': 'monster',
        'store_url': 'store_monster_card',
        'update_url': 'update_monster_card',
        'purge_url': 'purge_monster_card',
        'cards': app.card_system.monster_cards()
    }
    return render(request, "YuGiOh/cards.html", context)
