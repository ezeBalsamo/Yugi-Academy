from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.models import app
from YuGiOh.cards.forms import SpellCardForm
from YuGiOh.cards import SpellCard
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context_for(spell_card):
    return {
        'form': SpellCardForm(initial={
            'name': spell_card.name,
            'type': spell_card.type,
            'description': spell_card.description,
            'image': spell_card.image
        }),
        'action_name': 'Update',
        'button_content': 'Update'
    }


@login_required
def update_spell_card(request, spell_card_id):
    spell_card = app.card_system.spell_card_numbered(spell_card_id)
    context = context_for(spell_card)
    if request.method == 'POST':
        form = SpellCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                updated_spell_card = SpellCard.from_form(form.cleaned_data)
                app.card_system.update_spell_card_with(spell_card, updated_spell_card)
                messages.info(request, f'{spell_card} has been successfully updated.')
                return redirect('spell_cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render(request, 'YuGiOh/spell_card.html', context)
        else:
            messages.error(request, str(form.errors))
            return render(request, 'YuGiOh/spell_card.html', context)

    if request.method == 'GET':
        return render(request, 'YuGiOh/spell_card.html', context)

    raise Exception(f'The {request.method} method was not expected')
