import pytest

from YuGiOh.cards.src.spell_card import SpellCard
from utils.src.instance_creation_failed import InstanceCreationFailed


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
    spell_card = SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.')
    assert spell_card.name == 'Pot of Greed'
    assert spell_card.type == 'Normal'
    assert spell_card.description == 'Draw 2 cards.'
