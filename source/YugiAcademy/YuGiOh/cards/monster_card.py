from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.fields.files import ImageFieldFile

from .card import Card
from YuGiOh.booster_packs import BoosterPackCard
from assertions import enforce_not_blank, enforce_must_be_between, enforce_must_be_positive


class MonsterCard(Card):
    type_description = 'monster card'
    Attributes = models.TextChoices('Attributes', 'Dark Divine Earth Fire Light Water Wind')
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
              race: str,
              attribute: str,
              level: int,
              attack: int,
              defense: int,
              description: str,
              image: ImageFieldFile):
        enforce_not_blank(name, "Name")
        enforce_not_blank(race, "Race")
        enforce_not_blank(attribute, "Attribute")
        enforce_not_blank(description, "Description")
        enforce_must_be_between(1, level, 12, "Level")
        enforce_must_be_positive(attack, "Attack")
        enforce_must_be_positive(defense, "Defense")

        return cls(name=name,
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
                            race: str,
                            attribute: str,
                            level: int,
                            attack: int,
                            defense: int,
                            description: str):
        enforce_not_blank(name, "Name")
        enforce_not_blank(race, "Race")
        enforce_not_blank(attribute, "Attribute")
        enforce_not_blank(description, "Description")
        enforce_must_be_between(1, level, 12, "Level")
        enforce_must_be_positive(attack, "Attack")
        enforce_must_be_positive(defense, "Defense")

        return cls(name=name,
                   race=race,
                   attribute=attribute,
                   level=level,
                   attack=attack,
                   defense=defense,
                   description=description)
    
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
