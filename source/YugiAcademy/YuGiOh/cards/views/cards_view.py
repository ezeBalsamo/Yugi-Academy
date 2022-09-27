from django.shortcuts import render
from YuGiOh.models import card_system


def cards(request):
    context = {
        'monster_cards': card_system().monster_cards(),
        'spell_cards': card_system().spell_cards(),
        'trap_cards': card_system().trap_cards()
    }
    return render(request, "YuGiOh/cards.html", context)
