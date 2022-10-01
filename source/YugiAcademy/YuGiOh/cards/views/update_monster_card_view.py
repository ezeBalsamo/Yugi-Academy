from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.models import app
from YuGiOh.cards.forms import MonsterCardForm
from YuGiOh.cards import MonsterCard
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context_for(monster_card):
    return {
        'card_type': 'monster',
        'form': MonsterCardForm(initial={
            'name': monster_card.name,
            'race': monster_card.race,
            'attribute': monster_card.attribute,
            'level': monster_card.level,
            'attack': monster_card.attack,
            'defense': monster_card.defense,
            'description': monster_card.description,
            'image': monster_card.image
        }),
        'action_name': 'Update',
        'button_content': 'Update',
        'cards_url': 'monster_cards',
    }


@login_required
def update_monster_card(request, monster_card_id):
    monster_card = app.card_system.monster_card_numbered(monster_card_id)
    context = context_for(monster_card)
    if request.method == 'POST':
        form = MonsterCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                updated_monster_card = MonsterCard.from_form(form.cleaned_data)
                app.card_system.update_monster_card_with(monster_card, updated_monster_card)
                messages.info(request, f'{monster_card} has been successfully updated.')
                return redirect('spell_cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render(request, 'YuGiOh/card.html', context)
        else:
            messages.error(request, str(form.errors))
            return render(request, 'YuGiOh/card.html', context)

    if request.method == 'GET':
        return render(request, 'YuGiOh/card.html', context)

    raise Exception(f'The {request.method} method was not expected')
