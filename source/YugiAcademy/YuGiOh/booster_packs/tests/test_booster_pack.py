import pytest

from datetime import datetime

from assertions.instance_creation_failed import InstanceCreationFailed
from YuGiOh.booster_packs import BoosterPack


def test_booster_pack_name_must_not_be_blank():
    for invalid_name in ['', ' ']:
        with pytest.raises(InstanceCreationFailed) as exception_info:
            BoosterPack.named(name=invalid_name, code='LOB-EN', release_date=datetime(2002, 3, 8))
        assert exception_info.message_text() == 'Name must not be blank.'
