import pytest

from utils.src.instance_creation_failed import InstanceCreationFailed


def test_exception_raises():
    explanation = 'Testing failures'
    with pytest.raises(InstanceCreationFailed) as exception_info:
        raise InstanceCreationFailed(explanation)
    assert exception_info.message_text() == explanation
