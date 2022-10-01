from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.fields.files import ImageFieldFile

from .card import Card
from YuGiOh.booster_packs import BoosterPackCard
from assertions import enforce_not_blank, enforce_must_be_between, enforce_must_be_positive_or_zero, enforce_is_included_in


class MonsterCard(Card):
    type_description = 'monster card'
    Attributes = models.TextChoices('Attributes', 'Dark Divine Earth Fire Light Water Wind')
    Types = models.TextChoices('Types', 'Normal Effect Ritual Fusion Synchro Xyz Pendulum Link Token')
    type = models.CharField(max_length=10, choices=Types.choices)
    race = models.CharField(max_length=20)
    attribute = models.CharField(max_length=10, choices=Attributes.choices)
    level = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    set = GenericRelation(to=BoosterPackCard, related_query_name='monster_card')
    image = models.ImageField(upload_to='cards/monster_cards', default='cards/card-back.jpg')

    @classmethod
    def named(cls,
              name: str,
              type: str,
              race: str,
              attribute: str,
              level: int,
              attack: int,
              defense: int,
              description: str,
              image: ImageFieldFile):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_is_included_in(type, "Type", cls.Types)
        enforce_not_blank(race, "Race")
        enforce_not_blank(attribute, "Attribute")
        enforce_is_included_in(attribute, "Attribute", cls.Attributes)
        enforce_not_blank(description, "Description")
        enforce_must_be_between(1, level, 12, "Level")
        enforce_must_be_positive_or_zero(attack, "Attack")
        enforce_must_be_positive_or_zero(defense, "Defense")

        return cls(name=name,
                   type=type,
                   race=race,
                   attribute=attribute,
                   level=level,
                   attack=attack,
                   defense=defense,
                   description=description,
                   image=image)

    @classmethod
    def without_image_named(cls,
                            name: str,
                            type: str,
                            race: str,
                            attribute: str,
                            level: int,
                            attack: int,
                            defense: int,
                            description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(type, "Type")
        enforce_is_included_in(type, "Type", cls.Types)
        enforce_not_blank(race, "Race")
        enforce_not_blank(attribute, "Attribute")
        enforce_is_included_in(attribute, "Attribute", cls.Attributes)
        enforce_not_blank(description, "Description")
        enforce_must_be_between(1, level, 12, "Level")
        enforce_must_be_positive_or_zero(attack, "Attack")
        enforce_must_be_positive_or_zero(defense, "Defense")

        return cls(name=name,
                   type=type,
                   race=race,
                   attribute=attribute,
                   level=level,
                   attack=attack,
                   defense=defense,
                   description=description)

    @classmethod
    def from_form(cls, form_data):
        image = form_data.get('image')

        if image:
            return cls.named(name=form_data.get('name'),
                             type=form_data.get('type'),
                             race=form_data.get('race'),
                             attribute=form_data.get('attribute'),
                             level=form_data.get('level'),
                             attack=form_data.get('attack'),
                             defense=form_data.get('defense'),
                             description=form_data.get('description'),
                             image=image)

        return cls.without_image_named(name=form_data.get('name'),
                                       type=form_data.get('type'),
                                       race=form_data.get('race'),
                                       attribute=form_data.get('attribute'),
                                       level=form_data.get('level'),
                                       attack=form_data.get('attack'),
                                       defense=form_data.get('defense'),
                                       description=form_data.get('description'))
    
    def synchronize_with(self, monster_card):
        self.name = monster_card.name
        self.race = monster_card.race
        self.attribute = monster_card.attribute
        self.level = monster_card.level
        self.attack = monster_card.attack
        self.defense = monster_card.defense
        self.description = monster_card.description
        if monster_card.image.name != 'cards/card-back.jpg':
            self.image = monster_card.image
