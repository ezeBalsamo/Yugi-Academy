from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.models import app
from YuGiOh.booster_packs.forms import BoosterPackForm
from YuGiOh.booster_packs import BoosterPack
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context_for(booster_pack):
    return {
        'form': BoosterPackForm(initial={
            'name': booster_pack.name,
            'code': booster_pack.code,
            'release_date': booster_pack.release_date
        }),
        'action_name': 'Update',
        'button_content': 'Update'
    }


@login_required
def update_booster_pack(request, booster_pack_id):
    booster_pack = app.booster_pack_system.booster_pack_numbered(booster_pack_id)
    context = context_for(booster_pack)
    if request.method == 'POST':
        form = BoosterPackForm(request.POST)
        if form.is_valid():
            try:
                updated_booster_pack = BoosterPack.from_form(form.cleaned_data)
                app.booster_pack_system.update_booster_pack_with(booster_pack, updated_booster_pack)
                messages.info(request, f'{booster_pack} has been successfully updated.')
                return redirect('booster_packs')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render(request, 'YuGiOh/booster_pack.html', context)

    if request.method == 'GET':
        return render(request, 'YuGiOh/booster_pack.html', context)

    raise Exception(f'The {request.method} method was not expected')
