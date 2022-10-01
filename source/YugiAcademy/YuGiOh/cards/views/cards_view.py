from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from YuGiOh.models import app


@login_required
def spell_cards(request):
    context = {
        'cards': app.card_system.spell_cards()
    }
    return render(request, "YuGiOh/spell_cards.html", context)
