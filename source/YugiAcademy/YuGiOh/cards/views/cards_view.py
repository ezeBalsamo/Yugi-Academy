from django.shortcuts import render
from YuGiOh.models import app


def cards(request):
    context = {
        'monster_cards': app.card_system.monster_cards(),
        'spell_cards': app.card_system.spell_cards(),
        'trap_cards': app.card_system.trap_cards()
    }
    return render(request, "YuGiOh/cards.html", context)
