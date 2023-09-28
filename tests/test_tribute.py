import pytest

from game.logic.tribute import Tribute


def test_create_live_tribute_from_str():
    res = Tribute.from_string('t')
    assert res.__eq__(Tribute())


# Negative test
def test_create_tribute_error():
    with pytest.raises(ValueError):
        res = Tribute.from_string('-')

