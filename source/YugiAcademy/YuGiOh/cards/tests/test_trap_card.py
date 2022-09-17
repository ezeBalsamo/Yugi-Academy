import pytest

from assertions.instance_creation_failed import InstanceCreationFailed
from YuGiOh.cards.trap_card import TrapCard


def test_trap_card_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            TrapCard.named(name=invalid_name, type='Normal', description='Draw 1 card.')
        assert exception_info.message_text() == 'Name must not be blank.'


def test_spell_card_type_must_not_be_blank():
    for invalid_type in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            TrapCard.named(name='Pot of Greed', type=invalid_type, description='Draw 1 card.')
        assert exception_info.message_text() == 'Type must not be blank.'
