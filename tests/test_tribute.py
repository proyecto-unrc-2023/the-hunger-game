import pytest

from game.logic.district import District
from game.logic.tribute import Tribute


def test_create_live_tribute_from_str():
    res = Tribute.from_string('t')
    assert res.__eq__(Tribute())


# Negative test
def test_create_tribute_error():
    with pytest.raises(ValueError):
        res = Tribute.from_string('-')


def test_tribute_is_dead_or_is_alive():
    tribute = Tribute()
    tribute.life = 0
    assert tribute.is_dead().__eq__(True)
    tribute.life = 10
    assert tribute.is_alive().__eq__(True)


def test_tribute_to_string():
    district1 = District()
    tribute1 = Tribute()
    district1.set_config(50, 5, 1, 1, 5)
    tribute1.district = district1
    assert (tribute1.__str__()).__eq__('t1')


def test_set_config_tribute():
    tribute = Tribute()
    tribute.set_cofing(50, 2, 3, 5)
    assert tribute.life == 50
    assert tribute.force == 2
    assert tribute.alliance == 3
    assert tribute.district == 5
