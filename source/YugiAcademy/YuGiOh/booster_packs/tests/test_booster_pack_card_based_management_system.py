import pytest

from datetime import date
from YuGiOh.cards import CardManagementSystem, SpellCard, TrapCard
from YuGiOh.booster_packs import BoosterPackManagementSystem, BoosterPack, BoosterPackCard
from assertions import SystemRestrictionInfringed, DataInconsistencyFound, \
    assert_is_empty, assert_the_only_one_in, \
    with_the_only_one_in


def assert_booster_pack_card_was_updated(booster_pack_card, updated_booster_pack_card, managed_booster_pack_card):
    assert managed_booster_pack_card == booster_pack_card
    assert managed_booster_pack_card.card == updated_booster_pack_card.card
    assert managed_booster_pack_card.booster_pack == updated_booster_pack_card.booster_pack
    assert managed_booster_pack_card.identifier == updated_booster_pack_card.identifier
    assert managed_booster_pack_card.rarity == updated_booster_pack_card.rarity


@pytest.mark.django_db
class TestBoosterPackManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.card_system = CardManagementSystem()
        self.system = BoosterPackManagementSystem()

    def pot_of_greed(self):
        spell_card = SpellCard.named(name='Pot of Greed', type='Normal', description='Draw 2 cards.')
        self.card_system.store_spell_card(spell_card)
        return spell_card

    def sogen(self):
        spell_card = SpellCard.named(name="Sogen",
                                     type="Field",
                                     description="All Warrior and Beast-Warrior monsters on the field gain 200 ATK/DEF.")
        self.card_system.store_spell_card(spell_card)
        return spell_card

    def mirror_force(self):
        trap_card = TrapCard.named(name="Mirror Force",
                                   type="Normal",
                                   description="When an opponent's monster declares an attack: Destroy all your "
                                               "opponent's Attack Position monsters.")
        self.card_system.store_trap_card(trap_card)
        return trap_card

    def legend_of_blue_eyes_white_dragon(self):
        booster_pack = BoosterPack.named(name="Legend of Blue Eyes White Dragon",
                                         code='LOB-EN',
                                         release_date=date(2002, 3, 8))
        self.system.store_booster_pack(booster_pack)
        return booster_pack

    def metal_raiders(self):
        booster_pack = BoosterPack.named(name="Metal Raiders",
                                         code='MRD-EN',
                                         release_date=date(2002, 6, 26))
        self.system.store_booster_pack(booster_pack)
        return booster_pack

    def pot_of_greed_lob_en119(self):
        return BoosterPackCard.referring_to(card=self.pot_of_greed(),
                                            booster_pack=self.legend_of_blue_eyes_white_dragon(),
                                            identifier='LOB-EN119',
                                            rarity='Rare')

    def mirror_force_mrd_en138(self):
        return BoosterPackCard.referring_to(card=self.mirror_force(),
                                            booster_pack=self.metal_raiders(),
                                            identifier='MRD-EN138',
                                            rarity='Ultra Rare')

    def test_store_booster_pack_card(self):
        assert_is_empty(self.system.booster_pack_cards())
        booster_pack_card = self.pot_of_greed_lob_en119()
        self.system.store_booster_pack_card(booster_pack_card)
        assert_the_only_one_in(self.system.booster_pack_cards(), booster_pack_card)

    def test_cannot_store_booster_pack_card_when_there_is_one_with_same_identifier(self):
        booster_pack_card = self.pot_of_greed_lob_en119()
        another_booster_pack_card = BoosterPackCard.referring_to(card=self.sogen(),
                                                                 booster_pack=booster_pack_card.booster_pack,
                                                                 identifier=booster_pack_card.identifier,
                                                                 rarity='Common')
        self.system.store_booster_pack_card(booster_pack_card)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.store_booster_pack_card(another_booster_pack_card)
        assert exception_info.message_text() == 'There is already a booster pack card identified by LOB-EN119.'
        assert_the_only_one_in(self.system.booster_pack_cards(), booster_pack_card)

    def test_purge_booster_pack_card(self):
        booster_pack_card = self.pot_of_greed_lob_en119()
        self.system.store_booster_pack_card(booster_pack_card)
        assert_the_only_one_in(self.system.booster_pack_cards(), booster_pack_card)
        self.system.purge_booster_pack_card(booster_pack_card)
        assert_is_empty(self.system.booster_pack_cards())

    def test_cannot_purge_booster_pack_not_found(self):
        booster_pack_card = self.pot_of_greed_lob_en119()
        self.system.store_booster_pack_card(booster_pack_card)
        self.system.purge_booster_pack_card(booster_pack_card)
        with pytest.raises(DataInconsistencyFound) as exception_info:
            self.system.purge_booster_pack_card(booster_pack_card)
        assert exception_info.message_text() == 'Pot of Greed - LOB-EN119 was expected to be found, but it was not.'
        assert_is_empty(self.system.booster_pack_cards())

    def test_update_booster_pack_card(self):
        booster_pack_card = self.pot_of_greed_lob_en119()
        updated_booster_pack_card = self.mirror_force_mrd_en138()
        self.system.store_booster_pack_card(booster_pack_card)
        self.system.update_booster_pack_card_with(booster_pack_card, updated_booster_pack_card)
        with_the_only_one_in(self.system.booster_pack_cards(),
                             lambda managed_booster_pack_card: assert_booster_pack_card_was_updated(booster_pack_card,
                                                                                                    updated_booster_pack_card,
                                                                                                    managed_booster_pack_card))
