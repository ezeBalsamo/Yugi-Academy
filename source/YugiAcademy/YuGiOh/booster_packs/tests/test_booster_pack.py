import pytest

from datetime import date

from assertions import InstanceCreationFailed
from YuGiOh.booster_packs import BoosterPack


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
    booster_pack = BoosterPack.named(name='Legend of Blue Eyes White Dragon',
                                     code='LOB-EN',
                                     release_date=date(2002, 3, 8))
    assert booster_pack.name == 'Legend of Blue Eyes White Dragon'
    assert booster_pack.code == 'LOB-EN'
    assert booster_pack.release_date == date(2002, 3, 8)
