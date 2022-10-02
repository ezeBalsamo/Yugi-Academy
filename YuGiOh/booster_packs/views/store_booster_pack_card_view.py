from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.booster_packs.forms import BoosterPackCardForm
from YuGiOh.booster_packs import BoosterPackCard
from YuGiOh.models import app
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context_for(booster_pack):
    return {
        'form': BoosterPackCardForm(initial={
            'booster_pack': booster_pack
        }),
        'booster_pack': booster_pack,
        'action_name': 'Registration',
        'type_description': BoosterPackCard.type_description,
        'button_content': 'Register',
        'back_url': 'booster_pack_cards',
    }


def render_with(request, context):
    return render(request, 'YuGiOh/booster_pack_card.html', context)


def show_error_and_render_with(request, error, context):
    messages.error(request, str(error))
    return render_with(request, context)


@login_required
def store_booster_pack_card(request, booster_pack_id):
    booster_pack = app.booster_pack_system.booster_pack_numbered(booster_pack_id)
    context = context_for(booster_pack)
    if request.method == 'POST':
        form = BoosterPackCardForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                card = app.card_system.card_named(form_data.get('card'))
                booster_pack_card = BoosterPackCard.from_form(card, booster_pack, form.cleaned_data)
                app.booster_pack_system.store_booster_pack_card(booster_pack_card)
                messages.info(request, f'{booster_pack_card} has been successfully registered.')
                return redirect(f'/yugioh/booster-pack-cards/booster-pack/{booster_pack_id}')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                return show_error_and_render_with(request, error, context)
        else:
            return show_error_and_render_with(request, form.errors, context)

    if request.method == 'GET':
        return render_with(request, context)

    raise Exception(f'The {request.method} method was not expected')
