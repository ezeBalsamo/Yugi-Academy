import pytest

from YuGiOh.cards import MonsterCard
from assertions.instance_creation_failed import InstanceCreationFailed


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
