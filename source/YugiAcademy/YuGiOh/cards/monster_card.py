from django.db import models

from .card import Card
from assertions import enforce_not_blank


class MonsterCard(Card):
    Attributes = models.TextChoices('Attributes', 'Dark Divine Earth Fire Light Water Wind')
    race = models.CharField(max_length=20)
    attribute = models.CharField(max_length=10, choices=Attributes.choices)
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()

    @classmethod
    def named(cls, name: str, race: str, attribute: str, level: int, attack: int, defense: int, description: str):
        enforce_not_blank(name, "Name")

    def related_query_name(self):
        return 'monster_card'
