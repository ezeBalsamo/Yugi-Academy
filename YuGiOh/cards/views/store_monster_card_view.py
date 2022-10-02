from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.cards.forms import MonsterCardForm
from YuGiOh.cards import MonsterCard
from YuGiOh.models import app
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context():
    return {
        'card_type': 'monster',
        'form': MonsterCardForm(),
        'action_name': 'Registration',
        'button_content': 'Register',
        'cards_url': 'monster_cards',
    }


def render_with(request):
    return render(request, 'YuGiOh/card.html', context())


def show_error_and_render_with(request, error):
    messages.error(request, str(error))
    return render_with(request)


@login_required
def store_monster_card(request):
    if request.method == 'POST':
        form = MonsterCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                monster_card = MonsterCard.from_form(form.cleaned_data)
                app.card_system.store_monster_card(monster_card)
                messages.info(request, f'{monster_card} has been successfully registered.')
                return redirect('monster_cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                return show_error_and_render_with(request, error)
        else:
            return show_error_and_render_with(request, form.errors)

    if request.method == 'GET':
        return render_with(request)

    raise Exception(f'The {request.method} method was not expected')
