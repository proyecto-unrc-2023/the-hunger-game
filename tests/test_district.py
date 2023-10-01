import pytest

from game.logic.district import District
from game.logic.tribute import Tribute

# tests para metodo set_config(...)

def test_set_config_invalid_force():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(50, 100, 1, 3, 4)  # force 100


def test_set_config_invalid_alliance():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(50, 10, 11, 3, 4)  # aliance 11


def test_set_config_tributes():
    district = District()
    district.set_config(50, 10, 6, 1, 5)
    list_tributes = district.tributes
    for i in range(len(list_tributes)):
        assert list_tributes[i].life == 50
        assert list_tributes[i].force == 10
        assert list_tributes[i].alliance == 6
        assert list_tributes[i].district == 1


# tests para metodo add_tribute(..)

def test_add_tribute_valid():
    district = District()
    tribute = Tribute()
    district.add_tribute(tribute)
    assert tribute in district.tributes


def test_add_tribute_invalid():
    district = District()
    tribute = "Not is a tribute"
    with pytest.raises(ValueError):
        district.add_tribute(tribute)