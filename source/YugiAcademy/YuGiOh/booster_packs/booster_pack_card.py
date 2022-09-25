from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from assertions import enforce_not_blank, InstanceCreationFailed
from .booster_pack import BoosterPack


def enforce_are_related(identifier, booster_pack):
    if not identifier.startswith(booster_pack.code):
        raise InstanceCreationFailed(f'Identifier must be related to code of {booster_pack} ({booster_pack.code}).')


class BoosterPackCard(models.Model):
    type_description = 'booster pack card'
    booster_pack = models.ForeignKey(to=BoosterPack, on_delete=models.PROTECT)
    identifier = models.CharField(max_length=20, unique=True)
    rarity = models.CharField(max_length=20)
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    card = GenericForeignKey()

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    @classmethod
    def referring_to(cls, card, booster_pack: BoosterPack, identifier: str, rarity: str):
        enforce_not_blank(identifier, "Identifier")
        enforce_not_blank(rarity, "Rarity")
        enforce_are_related(identifier, booster_pack)

        return cls(card=card, booster_pack=booster_pack, identifier=identifier, rarity=rarity)

    def __str__(self):
        return f'{self.card_name()} - {self.identifier}'

    def card_name(self):
        return self.card.name

    def synchronize_with(self, booster_pack_card):
        self.card = booster_pack_card.card
        self.booster_pack = booster_pack_card.booster_pack
        self.identifier = booster_pack_card.identifier
        self.rarity = booster_pack_card.rarity

