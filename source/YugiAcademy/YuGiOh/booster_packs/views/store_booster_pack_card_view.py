from django.shortcuts import redirect, render

from YuGiOh.booster_packs.forms import BoosterPackCardForm
from YuGiOh.booster_packs import BoosterPackCard
from YuGiOh.models import app


def store_booster_pack_card(request):
    if request.method == 'POST':
        form = BoosterPackCardForm(request.POST)
        if form.is_valid():
            booster_pack_card = BoosterPackCard.from_form(form.cleaned_data)
            app.booster_pack_system.store_booster_pack_card(booster_pack_card)
            return redirect(f'/yugioh/booster-pack/{booster_pack_card.booster_pack.id}')

    if request.method == 'GET':
        context = {
            'form': BoosterPackCardForm()
        }
        return render(request, 'YuGiOh/store_booster_pack_card.html', context)

    raise Exception(f'The {request.method} method was not expected')
