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
    return render(request, 'YuGiOh/store_spell_card.html', context())


@login_required
def store_spell_card(request):
    if request.method == 'POST':
        form = SpellCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                spell_card = SpellCard.from_from(form.cleaned_data)
                app.card_system.store_spell_card(spell_card)
                return redirect('spell_cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render_with(request)
        else:
            messages.error(request, str(form.errors))
            return render_with(request)

    if request.method == 'GET':
        return render_with(request)

    raise Exception(f'The {request.method} method was not expected')
