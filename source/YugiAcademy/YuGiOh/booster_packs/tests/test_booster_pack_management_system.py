import pytest

from datetime import datetime
from YuGiOh.booster_packs import BoosterPackManagementSystem, BoosterPack
from assertions import assert_is_empty, assert_the_only_one_in


def legend_of_blue_eyes_white_dragon():
    return BoosterPack.named(name="Legend of Blue Eyes White Dragon", code='LOB-EN', release_date=datetime(2002, 3, 8))


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
