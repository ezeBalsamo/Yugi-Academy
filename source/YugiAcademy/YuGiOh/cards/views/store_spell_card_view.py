from django.contrib import messages
from django.shortcuts import redirect, render

from YuGiOh.cards.forms import SpellCardForm
from YuGiOh.cards import SpellCard
from YuGiOh.models import app
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def store_spell_card(request):
    if request.method == 'POST':
        form = SpellCardForm(request.POST)
        if form.is_valid():
            try:
                spell_card = SpellCard.from_from(form.cleaned_data)
                app.card_system.store_spell_card(spell_card)
                return redirect('cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                messages.error(request, str(error))
                return render(request, 'YuGiOh/store_spell_card.html', {form: SpellCardForm()})

    if request.method == 'GET':
        context = {
            'form': SpellCardForm()
        }
        return render(request, 'YuGiOh/store_spell_card.html', context)

    raise Exception(f'The {request.method} method was not expected')
