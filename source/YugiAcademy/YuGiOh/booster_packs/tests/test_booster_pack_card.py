import pytest

from datetime import datetime

from assertions.instance_creation_failed import InstanceCreationFailed
from YuGiOh.booster_packs import BoosterPack, BoosterPackCard
from YuGiOh.cards import SpellCard


def booster_pack():
    return BoosterPack.named(name='Legend of Blue Eyes White Dragon',
                             code='LOB-EN',
                             release_date=datetime(2002, 3, 8))


def pot_of_greed():
    return SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.')


def test_booster_pack_card_identifier_must_not_be_blank():
    for invalid_identifier in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            BoosterPackCard.referring_to(card=pot_of_greed(),
                                         booster_pack=booster_pack(),
                                         identifier=invalid_identifier,
                                         rarity='Rare')

        assert exception_info.message_text() == 'Identifier must not be blank.'


def test_booster_pack_card_rarity_must_not_be_blank():
    for invalid_rarity in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            BoosterPackCard.referring_to(card=pot_of_greed(),
                                         booster_pack=booster_pack(),
                                         identifier='LOB-EN119',
                                         rarity=invalid_rarity)

        assert exception_info.message_text() == 'Rarity must not be blank.'
