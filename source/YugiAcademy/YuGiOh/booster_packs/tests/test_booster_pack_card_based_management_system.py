import pytest

from datetime import date
from YuGiOh.cards import CardManagementSystem, SpellCard
from YuGiOh.booster_packs import BoosterPackManagementSystem, BoosterPack, BoosterPackCard
from assertions import assert_is_empty, assert_the_only_one_in


def pot_of_greed():
    return SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.')


def legend_of_blue_eyes_white_dragon():
    return BoosterPack.named(name="Legend of Blue Eyes White Dragon", code='LOB-EN', release_date=date(2002, 3, 8))


@pytest.mark.django_db
class TestBoosterPackManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.card_system = CardManagementSystem()
        self.system = BoosterPackManagementSystem()

    def pot_of_greed_lob_en119(self):
        spell_card = pot_of_greed()
        booster_pack = legend_of_blue_eyes_white_dragon()
        self.card_system.store_spell_card(spell_card)
        self.system.store_booster_pack(booster_pack)

        return BoosterPackCard.referring_to(card=spell_card,
                                            booster_pack=booster_pack,
                                            identifier='LOB-EN119',
                                            rarity='Rare')

    def test_store_booster_pack_card(self):
        assert_is_empty(self.system.booster_pack_cards())
        booster_pack_card = self.pot_of_greed_lob_en119()
        self.system.store_booster_pack_card(booster_pack_card)
        assert_the_only_one_in(self.system.booster_pack_cards(), booster_pack_card)
