from django.db import models

from .card import Card
from assertions import enforce_not_blank, enforce_must_be_between, enforce_must_be_positive


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

    def related_query_name(self):
        return 'monster_card'
