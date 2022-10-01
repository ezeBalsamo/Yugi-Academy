from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.models import app
from YuGiOh.cards.forms import TrapCardForm
from YuGiOh.cards import TrapCard
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context_for(trap_card):
    return {
        'card_type': 'spell',
        'form': TrapCardForm(initial={
            'name': trap_card.name,
            'type': trap_card.type,
            'description': trap_card.description,
            'image': trap_card.image
        }),
        'action_name': 'Update',
        'button_content': 'Update',
        'cards_url': 'trap_cards',
    }


@login_required
def update_trap_card(request, trap_card_id):
    trap_card = app.card_system.trap_card_numbered(trap_card_id)
    context = context_for(trap_card)
    if request.method == 'POST':
        form = TrapCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                updated_trap_card = TrapCard.from_form(form.cleaned_data)
                app.card_system.update_trap_card_with(trap_card, updated_trap_card)
                messages.info(request, f'{trap_card} has been successfully updated.')
                return redirect('trap_cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render(request, 'YuGiOh/card.html', context)
        else:
            messages.error(request, str(form.errors))
            return render(request, 'YuGiOh/card.html', context)

    if request.method == 'GET':
        return render(request, 'YuGiOh/card.html', context)

    raise Exception(f'The {request.method} method was not expected')
