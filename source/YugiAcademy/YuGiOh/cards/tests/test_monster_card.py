import pytest

from assertions.instance_creation_failed import InstanceCreationFailed
from YuGiOh.cards import MonsterCard


def test_monster_card_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name=invalid_name,
                              race='Spellcaster',
                              attribute='Dark',
                              level=7,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.')
        assert exception_info.message_text() == 'Name must not be blank.'


def test_monster_card_race_must_not_be_blank():
    for invalid_race in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              race=invalid_race,
                              attribute='Dark',
                              level=7,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.')
        assert exception_info.message_text() == 'Race must not be blank.'


def test_monster_card_attribute_must_not_be_blank():
    for invalid_attribute in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              race='Spellcaster',
                              attribute=invalid_attribute,
                              level=7,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.')
        assert exception_info.message_text() == 'Attribute must not be blank.'


def test_monster_card_level_must_between_1_and_12():
    for invalid_level in [-1, 0, 13]:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              race='Spellcaster',
                              attribute='Dark',
                              level=invalid_level,
                              attack=2500,
                              defense=2100,
                              description='The ultimate wizard in terms of attack and defense.')
        assert exception_info.message_text() == 'Level must be between 1 and 12.'


def test_monster_card_attack_must_be_positive():
    with pytest.raises(InstanceCreationFailed) as exception_info:
        MonsterCard.named(name='Dark Magician',
                          race='Spellcaster',
                          attribute='Dark',
                          level=7,
                          attack=-100,
                          defense=2100,
                          description='The ultimate wizard in terms of attack and defense.')
    assert exception_info.message_text() == 'Attack must be positive.'


def test_monster_card_defense_must_be_positive():
    with pytest.raises(InstanceCreationFailed) as exception_info:
        MonsterCard.named(name='Dark Magician',
                          race='Spellcaster',
                          attribute='Dark',
                          level=7,
                          attack=2500,
                          defense=-100,
                          description='The ultimate wizard in terms of attack and defense.')
    assert exception_info.message_text() == 'Defense must be positive.'


def test_monster_card_description_must_not_be_blank():
    for invalid_description in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            MonsterCard.named(name='Dark Magician',
                              race='Spellcaster',
                              attribute='Dark',
                              level=7,
                              attack=2500,
                              defense=2100,
                              description=invalid_description)
        assert exception_info.message_text() == 'Description must not be blank.'


def test_monster_card_instance_creation_and_accessing():
    monster_card = MonsterCard.named(name='Dark Magician',
                                     race='Spellcaster',
                                     attribute='Dark',
                                     level=7,
                                     attack=2500,
                                     defense=2100,
                                     description='The ultimate wizard in terms of attack and defense.')
    assert monster_card.name == 'Dark Magician'
    assert monster_card.race == 'Spellcaster'
    assert monster_card.attribute == 'Dark'
    assert monster_card.level == 7
    assert monster_card.attack == 2500
    assert monster_card.defense == 2100
    assert monster_card.description == 'The ultimate wizard in terms of attack and defense.'
