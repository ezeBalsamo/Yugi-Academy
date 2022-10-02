from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.fields.files import ImageFieldFile

from .card import Card
from YuGiOh.booster_packs import BoosterPackCard
from assertions import enforce_not_blank, enforce_is_included_in


class SpellCard(Card):
    type_description = 'spell card'
    Types = models.TextChoices('Types', 'Normal Equip Continuous Quick-Play Field Ritual')
    type = models.CharField(max_length=10, choices=Types.choices)
    set = GenericRelation(to=BoosterPackCard, related_query_name='spell_card')
    image = models.ImageField(upload_to='cards/spell_cards', default='cards/card-back.jpg')

    @classmethod
    def named(cls, name: str, type: str, description: str, image: ImageFieldFile):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_is_included_in(type, "Type", cls.Types)
        enforce_not_blank(description, "Description")

        return cls(name=name, type=type, description=description, image=image)

    @classmethod
    def without_image_named(cls, name, type, description):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_is_included_in(type, "Type", cls.Types)
        enforce_not_blank(description, "Description")

        return cls(name=name, type=type, description=description)

    @classmethod
    def from_form(cls, form_data):
        image = form_data.get('image')

        if image:
            return cls.named(name=form_data.get('name'),
                             type=form_data.get('type'),
                             description=form_data.get('description'),
                             image=image)

        return cls.without_image_named(name=form_data.get('name'),
                                       type=form_data.get('type'),
                                       description=form_data.get('description'))

    def synchronize_with(self, spell_card):
        self.name = spell_card.name
        self.type = spell_card.type
        self.description = spell_card.description
        if spell_card.image.name != 'cards/card-back.jpg':
            self.image = spell_card.image

