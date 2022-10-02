from django.apps import apps

from YuGiOh.cards import Card, MonsterCard, SpellCard, TrapCard
from YuGiOh.booster_packs import BoosterPack, BoosterPackCard

app = apps.get_app_config('YuGiOh')
