from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.cards.forms import SpellCardForm
from YuGiOh.cards import SpellCard
from YuGiOh.models import app
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context():
    return {
        'form': SpellCardForm(),
        'action_name': 'Registration',
        'button_content': 'Store'
    }


def render_with(request):
    return render(request, 'YuGiOh/spell_card.html', context())


def show_error_and_render_with(request, error):
    messages.error(request, str(error))
    return render_with(request)


@login_required
def store_spell_card(request):
    if request.method == 'POST':
        form = SpellCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                spell_card = SpellCard.from_form(form.cleaned_data)
                app.card_system.store_spell_card(spell_card)
                return redirect('spell_cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                return show_error_and_render_with(request, error)
        else:
            return show_error_and_render_with(request, form.errors)

    if request.method == 'GET':
        return render_with(request)

    raise Exception(f'The {request.method} method was not expected')
