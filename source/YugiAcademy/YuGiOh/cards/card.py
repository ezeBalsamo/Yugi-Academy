from abc import abstractmethod

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from YuGiOh.booster_packs.booster_pack_card import BoosterPackCard


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
