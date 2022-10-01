from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.fields.files import ImageFieldFile

from .card import Card
from YuGiOh.booster_packs import BoosterPackCard
from assertions import enforce_not_blank


class SpellCard(Card):
    type_description = 'spell card'
    type = models.CharField(max_length=20)
    set = GenericRelation(to=BoosterPackCard, related_query_name='spell_card')
    image = models.ImageField(upload_to='cards/spell_cards', default='cards/card-back.jpg')

    @classmethod
    def named(cls, name: str, type: str, description: str, image: ImageFieldFile):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_not_blank(description, "Description")

        return cls(name=name, type=type, description=description, image=image)

    @classmethod
    def from_from(cls, form_data):
        return cls.named(name=form_data.get('name'),
                         type=form_data.get('type'),
                         description=form_data.get('description'),
                         image=form_data.get('image'))

    def synchronize_with(self, spell_card):
        self.name = spell_card.name
        self.type = spell_card.type
        self.description = spell_card.description
        self.image = spell_card.image
