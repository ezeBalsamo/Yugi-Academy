from abc import abstractmethod

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from utils.src.instance_creation_failed import InstanceCreationFailed


def enforce_not_blank(string, name):
    if not string.strip():
        raise InstanceCreationFailed(f'{name} must not be blank.')


class BoosterPack(models.Model):
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class BoosterPackCard(models.Model):
    booster_pack = models.ForeignKey(to=BoosterPack, on_delete=models.PROTECT)
    identifier = models.CharField(max_length=20, unique=True)
    rarity = models.CharField(max_length=20)
    card_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    card_id = models.PositiveIntegerField()
    card = GenericForeignKey('card_type', 'card_id')

    def card_name(self):
        return self.card.name

    def booster_pack_name(self):
        return self.booster_pack.name

    def booster_pack_code(self):
        return self.booster_pack.code


class Card(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=8000)
    set = GenericRelation(to=BoosterPackCard)

    @abstractmethod
    def related_query_name(self):
        pass

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class MonsterCard(Card):
    Attributes = models.TextChoices('Attributes', 'Dark Divine Earth Fire Light Water Wind')
    race = models.CharField(max_length=20)
    attribute = models.CharField(max_length=10, choices=Attributes.choices)
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()

    def related_query_name(self):
        return 'monster_card'


class SpellCard(Card):
    type = models.CharField(max_length=20)

    @classmethod
    def named(cls, name: str, type: str, description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_not_blank(description, "Description")

        return cls(name=name, type=type, description=description)

    def related_query_name(self):
        return 'spell_card'


class TrapCard(Card):
    type = models.CharField(max_length=20)

    def related_query_name(self):
        return 'trap_card'
