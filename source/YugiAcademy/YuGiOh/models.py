from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


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
