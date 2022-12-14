import pytest
from django.db.models.fields.files import ImageFieldFile, FileField

from assertions import InstanceCreationFailed
from YuGiOh.cards import MonsterCard


def card_back_image():
    return ImageFieldFile(instance=None, field=FileField(), name='cards/card-back.jpg')


def assert_is_expected(monster_card, name, type, race, attribute, level, attack, defense, description, image):
    assert monster_card.name == name
    assert monster_card.type == type
    assert monster_card.race == race
    assert monster_card.attribute == attribute
    assert monster_card.level == level
    assert monster_card.attack == attack
    assert monster_card.defense == defense
    assert monster_card.description == description
    assert str(monster_card) == monster_card.name
    assert monster_card.image == image


def test_monster_card_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name=invalid_name,
                              type='Normal',
                              race='Spellcaster',
                              attribute='Dark',
                              level=7,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.',
                              image=card_back_image())
        assert exception_info.message_text() == 'Name must not be blank.'


def test_monster_card_type_must_not_be_blank():
    for invalid_type in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              type=invalid_type,
                              race='Spellcaster',
                              attribute='Dark',
                              level=7,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.',
                              image=card_back_image())
        assert exception_info.message_text() == 'Type must not be blank.'


def test_monster_card_type_must_be_a_valid_one():
    invalid_type = 'Invalid Type'
    with pytest.raises(InstanceCreationFailed) as exception_info:
        MonsterCard.named(name='Dark Magician',
                          type=invalid_type,
                          race='Spellcaster',
                          attribute='Dark',
                          level=7,
                          attack=2500,
                          defense=2100,
                          description='The ultimate wizard in terms of attack and defense.',
                          image=card_back_image())
    assert exception_info.message_text() == 'Type must be one of this: Normal, Effect, Ritual, Fusion, Synchro, Xyz, ' \
                                            'Pendulum, Link, Token.'


def test_monster_card_race_must_not_be_blank():
    for invalid_race in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              type='Normal',
                              race=invalid_race,
                              attribute='Dark',
                              level=7,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.',
                              image=card_back_image())
        assert exception_info.message_text() == 'Race must not be blank.'


def test_monster_card_attribute_must_not_be_blank():
    for invalid_attribute in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              type='Normal',
                              race='Spellcaster',
                              attribute=invalid_attribute,
                              level=7,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.',
                              image=card_back_image())
        assert exception_info.message_text() == 'Attribute must not be blank.'


def test_monster_card_attribute_must_be_a_valid_one():
    invalid_attribute = 'Invalid Attribute'
    with pytest.raises(InstanceCreationFailed) as exception_info:
        MonsterCard.named(name='Dark Magician',
                          type='Normal',
                          race='Spellcaster',
                          attribute=invalid_attribute,
                          level=7,
                          attack=2500,
                          defense=2100,
                          description='The ultimate wizard in terms of attack and defense.',
                          image=card_back_image())
    assert exception_info.message_text() == 'Attribute must be one of this: Dark, Divine, Earth, Fire, Light, Water, ' \
                                            'Wind.'


def test_monster_card_level_must_between_1_and_12():
    for invalid_level in [-1, 0, 13]:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              type='Normal',
                              race='Spellcaster',
                              attribute='Dark',
                              level=invalid_level,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.',
                              image=card_back_image())
        assert exception_info.message_text() == 'Level must be between 1 and 12.'


def test_monster_card_attack_must_be_greater_or_equal_than_zero():
    with pytest.raises(InstanceCreationFailed) as exception_info:
        MonsterCard.named(name='Dark Magician',
                          type='Normal',
                          race='Spellcaster',
                          attribute='Dark',
                          level=7,
                          attack=-100,
                          defense=2100,
                          description='The ultimate wizard in terms of attack and defense.',
                          image=card_back_image())
    assert exception_info.message_text() == 'Attack must be positive.'


def test_monster_card_defense_must_be_greater_or_equal_than_zero():
    with pytest.raises(InstanceCreationFailed) as exception_info:
        MonsterCard.named(name='Dark Magician',
                          type='Normal',
                          race='Spellcaster',
                          attribute='Dark',
                          level=7,
                          attack=2500,
                          defense=-100,
                          description='The ultimate wizard in terms of attack and defense.',
                          image=card_back_image())
    assert exception_info.message_text() == 'Defense must be positive.'


def test_monster_card_description_must_not_be_blank():
    for invalid_description in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              type='Normal',
                              race='Spellcaster',
                              attribute='Dark',
                              level=7,
                              attack=2500,
                              defense=2100,
                              description=invalid_description,
                              image=card_back_image())
        assert exception_info.message_text() == 'Description must not be blank.'


def test_monster_card_instance_creation_and_accessing():
    name = 'Dark Magician'
    type = 'Normal'
    race = 'Spellcaster'
    attribute = 'Dark'
    level = 7
    attack = 2500
    defense = 2100
    description = 'The ultimate wizard in terms of attack and defense.'
    image = card_back_image()
    monster_card = MonsterCard.named(name=name,
                                     type=type,
                                     race=race,
                                     attribute=attribute,
                                     level=level,
                                     attack=attack,
                                     defense=defense,
                                     description=description,
                                     image=image)
    assert_is_expected(monster_card, name, type, race, attribute, level, attack, defense, description, image)


def test_instance_creation_from_form_with_image():
    name = 'Dark Magician'
    type = 'Normal'
    race = 'Spellcaster'
    attribute = 'Dark'
    level = 7
    attack = 2500
    defense = 2100
    description = 'The ultimate wizard in terms of attack and defense.'
    image = card_back_image()
    monster_card = MonsterCard.from_form(locals())
    assert_is_expected(monster_card, name, type, race, attribute, level, attack, defense, description, image)


def test_instance_creation_from_form_without_image():
    name = 'Dark Magician'
    type = 'Normal'
    race = 'Spellcaster'
    attribute = 'Dark'
    level = 7
    attack = 2500
    defense = 2100
    description = 'The ultimate wizard in terms of attack and defense.'
    monster_card = MonsterCard.from_form(locals())
    assert_is_expected(monster_card, name, type, race, attribute, level, attack, defense, description,
                       card_back_image())
