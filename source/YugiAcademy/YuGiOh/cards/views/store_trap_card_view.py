from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from YuGiOh.cards.forms import TrapCardForm
from YuGiOh.cards import TrapCard
from YuGiOh.models import app
from assertions import InstanceCreationFailed, SystemRestrictionInfringed


def context():
    return {
        'card_type': 'trap',
        'form': TrapCardForm(),
        'action_name': 'Registration',
        'button_content': 'Store',
        'cards_url': 'trap_cards',
    }


def render_with(request):
    return render(request, 'YuGiOh/card.html', context())


def show_error_and_render_with(request, error):
    messages.error(request, str(error))
    return render_with(request)


@login_required
def store_trap_card(request):
    if request.method == 'POST':
        form = TrapCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                trap_card = TrapCard.from_form(form.cleaned_data)
                app.card_system.store_trap_card(trap_card)
                messages.info(request, f'{trap_card} has been successfully registered.')
                return redirect('trap_cards')
            except (InstanceCreationFailed, SystemRestrictionInfringed) as error:
                return show_error_and_render_with(request, error)
        else:
            return show_error_and_render_with(request, form.errors)

    if request.method == 'GET':
        return render_with(request)

    raise Exception(f'The {request.method} method was not expected')
