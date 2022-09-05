from django.shortcuts import render, redirect
from .models import MonsterCard, SpellCard, TrapCard, BoosterPack, BoosterPackCard
from .forms import SpellCardForm, SearchBoosterPackForm, BoosterPackForm, BoosterPackCardForm


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


def find_or_store_spell_card(request):
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


def find_or_store_booster_pack(request):
    if request.method == 'POST':
        form = BoosterPackForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            booster_pack = \
                BoosterPack(name=form_data.get('name'),
                            code=form_data.get('code'),
                            release_date=form_data.get('release_date'))
            booster_pack.save()
            return redirect('booster_packs')

    if request.method == 'GET':
        context = {
            'form': BoosterPackForm()
        }
        return render(request, 'YuGiOh/booster_pack_registration.html', context)

    raise Exception(f'The {request.method} method was not expected')


def booster_pack_cards(request, booster_pack_id: id):
    booster_pack = BoosterPack.objects.get(id=booster_pack_id)
    context = {
        'booster_pack': booster_pack,
        'booster_pack_cards': BoosterPackCard.objects.filter(booster_pack=booster_pack)
    }
    return render(request, "YuGiOh/booster_pack_cards.html", context)


def find_or_store_booster_pack_card(request):
    if request.method == 'POST':
        form = BoosterPackCardForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            booster_pack = form_data.get('booster_pack')
            booster_pack_card = \
                BoosterPackCard(card=form_data.get('card'),
                                booster_pack=booster_pack,
                                identifier=form_data.get('identifier'),
                                rarity=form_data.get('rarity'))
            booster_pack_card.save()
            return redirect(f'/yugioh/booster-pack/{booster_pack.id}')

    if request.method == 'GET':
        context = {
            'form': BoosterPackCardForm()
        }
        return render(request, 'YuGiOh/booster_pack_card_registration.html', context)

    raise Exception(f'The {request.method} method was not expected')


def delete_booster_pack_card(request, booster_pack_card_id: int):
    booster_pack_card = BoosterPackCard.objects.get(id=booster_pack_card_id)
    booster_pack = booster_pack_card.booster_pack
    booster_pack_card.delete()
    return redirect(f'/yugioh/booster-pack/{booster_pack.id}')
