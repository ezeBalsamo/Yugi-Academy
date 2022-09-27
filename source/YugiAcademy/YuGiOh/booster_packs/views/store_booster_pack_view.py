from django.shortcuts import redirect, render

from YuGiOh.booster_packs.forms import BoosterPackForm
from YuGiOh.booster_packs import BoosterPack
from YuGiOh.models import app


def store_booster_pack(request):
    if request.method == 'POST':
        form = BoosterPackForm(request.POST)
        if form.is_valid():
            booster_pack = BoosterPack.from_form(form.cleaned_data)
            app.booster_pack_system.store_booster_pack(booster_pack)
            return redirect('booster-packs')

    if request.method == 'GET':
        context = {
            'form': BoosterPackForm()
        }
        return render(request, 'YuGiOh/store_booster_pack.html', context)

    raise Exception(f'The {request.method} method was not expected')
