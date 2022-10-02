import pytest

from datetime import date

from assertions import InstanceCreationFailed
from YuGiOh.booster_packs import BoosterPack


def assert_is_expected(booster_pack, name, code, release_date):
    assert booster_pack.name == name
    assert booster_pack.code == code
    assert booster_pack.release_date == release_date


def test_booster_pack_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            BoosterPack.named(name=invalid_name, code='LOB-EN', release_date=date(2002, 3, 8))
        assert exception_info.message_text() == 'Name must not be blank.'


def test_booster_pack_code_must_not_be_blank():
    for invalid_code in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            BoosterPack.named(name='Legend of Blue Eyes White Dragon', code='', release_date=date(2002, 3, 8))
        assert exception_info.message_text() == 'Code must not be blank.'


def test_instance_creation_and_accessing():
    name = 'Legend of Blue Eyes White Dragon'
    code = 'LOB-EN'
    release_date = date(2002, 3, 8)
    booster_pack = BoosterPack.named(name=name, code=code, release_date=release_date)
    assert_is_expected(booster_pack, name, code, release_date)


def test_instance_creation_from_form():
    name = 'Legend of Blue Eyes White Dragon'
    code = 'LOB-EN'
    release_date = date(2002, 3, 8)
    booster_pack = BoosterPack.from_form(locals())
    assert_is_expected(booster_pack, name, code, release_date)
