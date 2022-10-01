import pytest
from django.db.models.fields.files import ImageFieldFile, FileField

from assertions import InstanceCreationFailed
from YuGiOh.cards import SpellCard


def card_back_image():
    return ImageFieldFile(instance=None, field=FileField(), name='cards/card-back.jpg')


def assert_is_expected(spell_card, name, type, description, image):
    assert spell_card.name == name
    assert spell_card.type == type
    assert spell_card.description == description
    assert str(spell_card) == spell_card.name
    assert spell_card.image == image


def test_spell_card_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            SpellCard.named(name=invalid_name, type='Normal', description='Draw 2 cards.', image=card_back_image())
        assert exception_info.message_text() == 'Name must not be blank.'


def test_spell_card_type_must_not_be_blank():
    for invalid_type in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            SpellCard.named(name='Pot of Greed', type=invalid_type, description='Draw 2 cards.',
                            image=card_back_image())
        assert exception_info.message_text() == 'Type must not be blank.'


def test_spell_card_description_must_not_be_blank():
    for invalid_description in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            SpellCard.named(name='Pot of Greed', type='Normal', description=invalid_description,
                            image=card_back_image())
        assert exception_info.message_text() == 'Description must not be blank.'


def test_instance_creation_and_accessing():
    name = 'Pot of Greed'
    type = 'Normal'
    description = 'Draw 2 cards'
    image = card_back_image()
    spell_card = SpellCard.named(name=name, type=type, description=description, image=image)
    assert_is_expected(spell_card, name, type, description, image)


def test_instance_creation_from_form_with_image():
    name = 'Pot of Greed'
    type = 'Normal'
    description = 'Draw 2 cards'
    image = card_back_image()
    spell_card = SpellCard.from_form(locals())
    assert_is_expected(spell_card, name, type, description, image)


def test_instance_creation_from_form_without_image():
    name = 'Pot of Greed'
    type = 'Normal'
    description = 'Draw 2 cards'
    spell_card = SpellCard.from_form(locals())
    assert_is_expected(spell_card, name, type, description, card_back_image())
