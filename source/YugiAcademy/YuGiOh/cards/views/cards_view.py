from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from YuGiOh.models import app


@login_required
def cards(request):
    context = {
        'monster_cards': app.card_system.monster_cards(),
        'spell_cards': app.card_system.spell_cards(),
        'trap_cards': app.card_system.trap_cards()
    }
    return render(request, "YuGiOh/cards.html", context)
