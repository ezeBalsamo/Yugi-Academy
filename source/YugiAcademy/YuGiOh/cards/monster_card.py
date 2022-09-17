from django.db import models

from YuGiOh.models import Card


class MonsterCard(Card):
    Attributes = models.TextChoices('Attributes', 'Dark Divine Earth Fire Light Water Wind')
    race = models.CharField(max_length=20)
    attribute = models.CharField(max_length=10, choices=Attributes.choices)
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()

    def related_query_name(self):
        return 'monster_card'
