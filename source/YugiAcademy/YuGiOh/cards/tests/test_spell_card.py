import pytest

from assertions import InstanceCreationFailed
from YuGiOh.cards import SpellCard


def assert_is_expected(spell_card, name, type, description):
    assert spell_card.name == name
    assert spell_card.type == type
    assert spell_card.description == description
    assert str(spell_card) == spell_card.name


def test_spell_card_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            SpellCard.named(name=invalid_name, type='Normal', description='Draw 2 cards.')
        assert exception_info.message_text() == 'Name must not be blank.'


def test_spell_card_type_must_not_be_blank():
    for invalid_type in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            SpellCard.named(name='Pot of Greed', type=invalid_type, description='Draw 2 cards.')
        assert exception_info.message_text() == 'Type must not be blank.'


def test_spell_card_description_must_not_be_blank():
    for invalid_description in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            SpellCard.named(name='Pot of Greed', type='Normal', description=invalid_description)
        assert exception_info.message_text() == 'Description must not be blank.'


def test_instance_creation_and_accessing():
    name = 'Pot of Greed'
    type = 'Normal'
    description = 'Draw 2 cards'
    spell_card = SpellCard.named(name=name, type=type, description=description)
    assert_is_expected(spell_card, name, type, description)


def test_instance_creation_from_form():
    name = 'Pot of Greed'
    type = 'Normal'
    description = 'Draw 2 cards'
    spell_card = SpellCard.from_from(locals())
    assert_is_expected(spell_card, name, type, description)
