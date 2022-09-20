from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from assertions import enforce_not_blank
from assertions.instance_creation_failed import InstanceCreationFailed
from .booster_pack import BoosterPack


def enforce_are_related(identifier, booster_pack):
    if not identifier.startswith(booster_pack.code):
        raise InstanceCreationFailed(f'Identifier must be related to code of {booster_pack} ({booster_pack.code}).')


class BoosterPackCard(models.Model):
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

    def card_name(self):
        return self.card.name
