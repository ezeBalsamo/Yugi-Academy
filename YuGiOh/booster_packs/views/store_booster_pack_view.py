from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.booster_packs.forms import BoosterPackForm
from YuGiOh.booster_packs import BoosterPack
from YuGiOh.models import app
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context():
    return {
        'form': BoosterPackForm(),
        'action_name': 'Registration',
        'button_content': 'Register'
    }


@login_required
def store_booster_pack(request):
    if request.method == 'POST':
        form = BoosterPackForm(request.POST)
        if form.is_valid():
            try:
                booster_pack = BoosterPack.from_form(form.cleaned_data)
                app.booster_pack_system.store_booster_pack(booster_pack)
                messages.info(request, f'{booster_pack} has been successfully registered.')
                return redirect('booster_packs')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render(request, 'YuGiOh/booster_pack.html', context())

    if request.method == 'GET':
        return render(request, 'YuGiOh/booster_pack.html', context())

    raise Exception(f'The {request.method} method was not expected')
