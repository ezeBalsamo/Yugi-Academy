import pytest

from utils.src.instance_creation_failed import InstanceCreationFailed
from YuGiOh.models import SpellCard


def test_spell_card_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            SpellCard.named(name=invalid_name, type='Normal', description='Draw 2 cards.')
        assert exception_info.message_text() == 'Name must not be blank.'

