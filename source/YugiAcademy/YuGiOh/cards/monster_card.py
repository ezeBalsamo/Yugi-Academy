from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .card import Card
from YuGiOh.booster_packs import BoosterPackCard
from assertions import enforce_not_blank, enforce_must_be_between, enforce_must_be_positive


class MonsterCard(Card):
    type_description = 'monster card'
    Attributes = models.TextChoices('Attributes', 'Dark Divine Earth Fire Light Water Wind')
    race = models.CharField(max_length=20)
    attribute = models.CharField(max_length=10, choices=Attributes.choices)
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    set = GenericRelation(to=BoosterPackCard, related_query_name='monster_card')

    @classmethod
    def named(cls, name: str, race: str, attribute: str, level: int, attack: int, defense: int, description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(race, "Race")
        enforce_not_blank(attribute, "Attribute")
        enforce_not_blank(description, "Description")
        enforce_must_be_between(1, level, 12, "Level")
        enforce_must_be_positive(attack, "Attack")
        enforce_must_be_positive(defense, "Defense")

        return cls(name=name,
                   race=race,
                   attribute=attribute,
                   level=level,
                   attack=attack,
                   defense=defense,
                   description=description)
