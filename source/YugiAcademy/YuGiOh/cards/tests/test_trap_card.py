import pytest
from django.db.models.fields.files import ImageFieldFile, FileField

from assertions import InstanceCreationFailed
from YuGiOh.cards import TrapCard


def card_back_image():
    return ImageFieldFile(instance=None, field=FileField(), name='cards/card-back.jpg')


def assert_is_expected(trap_card, name, type, description, image):
    assert trap_card.name == name
    assert trap_card.type == type
    assert trap_card.description == description
    assert str(trap_card) == trap_card.name
    assert trap_card.image == image


def test_trap_card_type_must_not_be_blank():
    for invalid_type in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            TrapCard.named(name='Jar of Greed', type=invalid_type, description='Draw 1 card.', image=card_back_image())
        assert exception_info.message_text() == 'Type must not be blank.'


def test_trap_card_type_must_be_a_valid_one():
    invalid_type = 'Invalid Type'
    with pytest.raises(InstanceCreationFailed) as exception_info:
        TrapCard.named(name='Jar of Greed', type=invalid_type, description='Draw 1 card.', image=card_back_image())
    assert exception_info.message_text() == 'Type must be one of this: Normal, Continuous, Counter, Equip, Field.'


def test_trap_card_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            TrapCard.named(name=invalid_name, type='Normal', description='Draw 1 card.', image=card_back_image())
        assert exception_info.message_text() == 'Name must not be blank.'


def test_trap_card_description_must_not_be_blank():
    for invalid_description in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            TrapCard.named(name='Jar of Greed', type='Normal', description=invalid_description, image=card_back_image())
        assert exception_info.message_text() == 'Description must not be blank.'


def test_instance_creation_and_accessing():
    name = 'Jar of Greed'
    type = 'Normal'
    description = 'Draw 1 card.'
    image = card_back_image()
    trap_card = TrapCard.named(name=name, type=type, description=description, image=image)
    assert_is_expected(trap_card, name, type, description, image)
