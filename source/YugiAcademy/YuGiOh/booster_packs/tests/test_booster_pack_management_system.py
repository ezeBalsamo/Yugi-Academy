import pytest

from datetime import date
from YuGiOh.booster_packs import BoosterPackManagementSystem, BoosterPack
from assertions import SystemRestrictionInfringed, DataInconsistencyFound, \
    assert_is_empty, assert_the_only_one_in, \
    with_the_only_one_in


def legend_of_blue_eyes_white_dragon():
    return BoosterPack.named(name="Legend of Blue Eyes White Dragon", code='LOB-EN', release_date=date(2002, 3, 8))


def metal_raiders():
    return BoosterPack.named(name="Metal Raiders", code='MRD-EN', release_date=date(2002, 6, 26))


def assert_booster_pack_was_updated(booster_pack, updated_booster_pack, managed_booster_pack):
    assert managed_booster_pack == booster_pack
    assert managed_booster_pack.name == updated_booster_pack.name
    assert managed_booster_pack.code == updated_booster_pack.code
    assert managed_booster_pack.release_date == updated_booster_pack.release_date


@pytest.mark.django_db
class TestBoosterPackManagementSystem:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.system = BoosterPackManagementSystem()

    def test_store_booster_pack(self):
        assert_is_empty(self.system.booster_packs())
        booster_pack = legend_of_blue_eyes_white_dragon()
        self.system.store_booster_pack(booster_pack)
        assert_the_only_one_in(self.system.booster_packs(), booster_pack)

    def test_cannot_store_booster_pack_when_there_is_one_with_same_name(self):
        booster_pack = legend_of_blue_eyes_white_dragon()
        another_booster_pack = BoosterPack.named(name=booster_pack.name,
                                                 code='MRD-EN',
                                                 release_date=date(2002, 6, 26))
        self.system.store_booster_pack(booster_pack)
        with pytest.raises(SystemRestrictionInfringed) as exception_info:
            self.system.store_booster_pack(another_booster_pack)
        assert exception_info.message_text() == 'There is already a booster pack named Legend of Blue Eyes White ' \
                                                'Dragon.'
        assert_the_only_one_in(self.system.booster_packs(), booster_pack)

    def test_purge_booster_pack(self):
        booster_pack = legend_of_blue_eyes_white_dragon()
        self.system.store_booster_pack(booster_pack)
        assert_the_only_one_in(self.system.booster_packs(), booster_pack)
        self.system.purge_booster_pack(booster_pack)
        assert_is_empty(self.system.booster_packs())

    def test_cannot_purge_booster_pack_not_found(self):
        booster_pack = legend_of_blue_eyes_white_dragon()
        self.system.store_booster_pack(booster_pack)
        self.system.purge_booster_pack(booster_pack)
        with pytest.raises(DataInconsistencyFound) as exception_info:
            self.system.purge_booster_pack(booster_pack)
        assert exception_info.message_text() == 'Legend of Blue Eyes White Dragon was expected to be found, but it ' \
                                                'was not.'
        assert_is_empty(self.system.booster_packs())

    def test_update_booster_pack(self):
        booster_pack = legend_of_blue_eyes_white_dragon()
        updated_booster_pack = metal_raiders()
        self.system.store_booster_pack(booster_pack)
        self.system.update_booster_pack_with(booster_pack, updated_booster_pack)
        with_the_only_one_in(self.system.booster_packs(),
                             lambda managed_booster_pack: assert_booster_pack_was_updated(booster_pack,
                                                                                          updated_booster_pack,
                                                                                          managed_booster_pack))
