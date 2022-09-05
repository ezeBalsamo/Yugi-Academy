from django.shortcuts import render, redirect
from .models import MonsterCard, SpellCard, TrapCard
from .forms import SpellCardForm


def home(request):
    return render(request, "YuGiOh/index.html")


def cards(request):
    context = {
        'monster_cards': MonsterCard.objects.all(),
        'spell_cards': SpellCard.objects.all(),
        'trap_cards': TrapCard.objects.all()
    }
    return render(request, "YuGiOh/cards.html", context)


def register_spell_card(request):
    if request.method == 'POST':
        form = SpellCardForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            spell_card = \
                SpellCard(name=form_data.get('name'),
                          type=form_data.get('type'),
                          description=form_data.get('description'))
            spell_card.save()
            return redirect('cards')

    if request.method == 'GET':
        context = {
            'form': SpellCardForm()
        }
        return render(request, 'YuGiOh/spell_card_registration.html', context)

    raise Exception(f'The {request.method} method was not expected')


def about(request):
    return render(request, "YuGiOh/about.html")


def login(request):
    return render(request, "YuGiOh/login.html")
