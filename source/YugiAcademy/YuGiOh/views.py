from django.shortcuts import render, redirect
from .models import MonsterCard, SpellCard, TrapCard, BoosterPack
from .forms import SpellCardForm, SearchBoosterPackForm


def home(request):
    return render(request, "YuGiOh/index.html")


def login(request):
    return render(request, "YuGiOh/login.html")


def about(request):
    return render(request, "YuGiOh/about.html")


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


def booster_packs_according_to(request):

    if request.method == 'POST':
        form = SearchBoosterPackForm(request.POST)
        if form.is_valid():
            partial_name = form.cleaned_data.get('name')
            return BoosterPack.objects.filter(name__icontains=partial_name)
        else:
            raise Exception(f'The {form} is not valid.')

    if request.method == 'GET':
        return []

    raise Exception(f'The {request.method} method was not expected')


def booster_packs(request):
    context = {
        'form': SearchBoosterPackForm(),
        'booster_packs': booster_packs_according_to(request)
    }
    return render(request, "YuGiOh/booster_packs.html", context)