import pytest

from datetime import date

from django.db.models.fields.files import ImageFieldFile, FileField

from assertions import InstanceCreationFailed
from YuGiOh.booster_packs import BoosterPack, BoosterPackCard
from YuGiOh.cards import SpellCard, TrapCard, MonsterCard


def card_back_image():
    return ImageFieldFile(instance=None, field=FileField(), name='cards/card-back.jpg')


def legend_of_blue_eyes_white_dragon():
    return BoosterPack.named(name='Legend of Blue Eyes White Dragon',
                             code='LOB-EN',
                             release_date=date(2002, 3, 8))


def pot_of_greed():
    return SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.', image=card_back_image())


def jar_of_greed():
    return TrapCard.named(name='Jar of Greed', type='Normal', description='Draw 1 card.', image=card_back_image())


def dark_magician():
    return MonsterCard.named(name='Dark Magician',
                             type='Normal',
                             race='Spellcaster',
                             attribute='Dark',
                             level=7,
                             attack=2500,
                             defense=2100,
                             description='The ultimate wizard in terms of attack and defense.',
                             image=card_back_image())


def assert_is_expected(booster_pack_card, card, booster_pack, identifier, rarity):
    assert booster_pack_card.card == card
    assert booster_pack_card.booster_pack == booster_pack
    assert booster_pack_card.identifier == identifier
    assert booster_pack_card.rarity == rarity

    assert booster_pack_card.card_name() == card.name
    assert booster_pack_card.card_type() == card.type
    assert booster_pack_card.card_type_description() == card.type_description


def test_booster_pack_card_identifier_must_not_be_blank():
    for invalid_identifier in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            BoosterPackCard.referring_to(card=pot_of_greed(),
                                         booster_pack=legend_of_blue_eyes_white_dragon(),
                                         identifier=invalid_identifier,
                                         rarity='Rare')

        assert exception_info.message_text() == 'Identifier must not be blank.'


def test_booster_pack_card_rarity_must_not_be_blank():
    for invalid_rarity in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            BoosterPackCard.referring_to(card=pot_of_greed(),
                                         booster_pack=legend_of_blue_eyes_white_dragon(),
                                         identifier='LOB-EN119',
                                         rarity=invalid_rarity)

        assert exception_info.message_text() == 'Rarity must not be blank.'


def test_booster_pack_card_identifier_must_be_related_to_booster_pack_code():
    with pytest.raises(InstanceCreationFailed) as exception_info:
        BoosterPackCard.referring_to(card=pot_of_greed(),
                                     booster_pack=legend_of_blue_eyes_white_dragon(),
                                     identifier='XXX-1234',
                                     rarity='Rare')

    assert exception_info.message_text() == \
           'Identifier must be related to code of Legend of Blue Eyes White Dragon (LOB-EN).'


@pytest.mark.django_db
def test_booster_pack_card_instance_creation_and_accessing():
    for card in [pot_of_greed(), jar_of_greed(), dark_magician()]:
        booster_pack = legend_of_blue_eyes_white_dragon()
        identifier = 'LOB-EN119'
        rarity = 'Rare'
        booster_pack_card = BoosterPackCard.referring_to(card=card,
                                                         booster_pack=booster_pack,
                                                         identifier=identifier,
                                                         rarity=rarity)
        assert_is_expected(booster_pack_card, card, booster_pack, identifier, rarity)


@pytest.mark.django_db
def test_booster_pack_card_instance_creation_from_form():
    for card in [pot_of_greed(), jar_of_greed(), dark_magician()]:
        booster_pack = legend_of_blue_eyes_white_dragon()
        identifier = 'LOB-EN119'
        rarity = 'Rare'
        form_data = {
            'identifier': identifier,
            'rarity': rarity
        }
        booster_pack_card = BoosterPackCard.from_form(card=card, booster_pack=booster_pack, form_data=form_data)
        assert_is_expected(booster_pack_card, card, booster_pack, identifier, rarity)
