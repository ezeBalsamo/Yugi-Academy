from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from YuGiOh.cards import CardManagementSystem, MonsterCard, SpellCard, TrapCard
from YuGiOh.booster_packs import BoosterPackManagementSystem, BoosterPack, BoosterPackCard
from .forms import SpellCardForm, SearchBoosterPackForm, BoosterPackForm, BoosterPackCardForm


def systems() -> tuple[CardManagementSystem, BoosterPackManagementSystem]:
    app = apps.get_app_config('YuGiOh')
    return app.card_system, app.booster_pack_system


card_system, booster_pack_system = systems()


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def cards(request):
    context = {
        'monster_cards': card_system.monster_cards(),
        'spell_cards': card_system.spell_cards(),
        'trap_cards': card_system.trap_cards()
    }
    return render(request, "YuGiOh/cards.html", context)


def find_or_store_spell_card(request):
    if request.method == 'POST':
        form = SpellCardForm(request.POST)
        if form.is_valid():
            spell_card = SpellCard.from_from(form.cleaned_data)
            card_system.store_spell_card(spell_card)
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
            return booster_pack_system.booster_pack_named_like(partial_name)
        else:
            raise Exception(f'The {form} is not valid.')

    if request.method == 'GET':
        return list()

    raise Exception(f'The {request.method} method was not expected')


@login_required
def booster_packs(request):
    context = {
        'form': SearchBoosterPackForm(),
        'booster_packs': booster_packs_according_to(request)
    }
    return render(request, "YuGiOh/booster_packs.html", context)


def find_or_store_booster_pack(request):
    if request.method == 'POST':
        form = BoosterPackForm(request.POST)
        if form.is_valid():
            booster_pack = BoosterPack.form_form(form.cleaned_data)
            booster_pack_system.store_booster_pack(booster_pack)
            return redirect('booster-packs')

    if request.method == 'GET':
        context = {
            'form': BoosterPackForm()
        }
        return render(request, 'YuGiOh/booster_pack_registration.html', context)

    raise Exception(f'The {request.method} method was not expected')


def booster_pack_cards(request, booster_pack_id: id):
    booster_pack = booster_pack_system.booster_pack_numbered(booster_pack_id)

    context = {
        'booster_pack': booster_pack,
        'booster_pack_cards': booster_pack_system.booster_pack_card_in(booster_pack)
    }
    return render(request, "YuGiOh/booster_pack_cards.html", context)


def find_or_store_booster_pack_card(request):
    if request.method == 'POST':
        form = BoosterPackCardForm(request.POST)
        if form.is_valid():
            booster_pack_card = BoosterPackCard.from_form(form.cleaned_data)
            booster_pack_system.store_booster_pack_card(booster_pack_card)
            return redirect(f'/yugioh/booster-pack/{booster_pack_card.booster_pack.id}')

    if request.method == 'GET':
        context = {
            'form': BoosterPackCardForm()
        }
        return render(request, 'YuGiOh/booster_pack_card_registration.html', context)

    raise Exception(f'The {request.method} method was not expected')


def delete_booster_pack_card(request, booster_pack_card_id: int):
    booster_pack_card = booster_pack_system.booster_pack_card_numbered(booster_pack_card_id)
    booster_pack_system.purge_booster_pack_card(booster_pack_card)
    return redirect(f'/yugioh/booster-pack/{booster_pack_card.booster_pack.id}')
