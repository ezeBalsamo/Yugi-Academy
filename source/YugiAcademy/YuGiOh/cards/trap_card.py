from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from .card import Card
from YuGiOh.booster_packs import BoosterPackCard
from assertions import enforce_not_blank


class TrapCard(Card):
    type = models.CharField(max_length=20)
    set = GenericRelation(to=BoosterPackCard, related_query_name='trap_card')

    @classmethod
    def named(cls, name: str, type: str, description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_not_blank(description, "Description")

        return cls(name=name, type=type, description=description)

    def synchronize_with(self, trap_card):
        self.name = trap_card.name
        self.type = trap_card.type
        self.description = trap_card.description
