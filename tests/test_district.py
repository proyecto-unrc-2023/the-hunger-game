import pytest

from game.logic.district import District
from game.logic.tribute import Tribute, LIFE_DEFAULT, COWARDICE_DEFAULT


def test_set_config_tributes():
    district = District()
    district.set_config(50, 15, 6, 0, 5, 3)
    list_tributes = district.tributes
    for i in range(len(list_tributes)):
        assert list_tributes[i].life == 50
        assert list_tributes[i].force == 15
        assert list_tributes[i].alliance == 6
        assert list_tributes[i].district == 0
        assert list_tributes[i].cowardice == 3


def test_set_config_random_tributes():
    district = District()
    num_district = 4
    district.set_config_random(num_district)
    for i in range(district.cant_tributes):
        assert district.tributes[i].life == LIFE_DEFAULT
        assert district.tributes[i].force + district.tributes[i].alliance <= 15
        assert district.tributes[i].district == num_district
        assert district.tributes[i].cowardice == COWARDICE_DEFAULT


def test_add_tribute_valid():
    district = District()
    district.cant_tributes = 0
    tribute = Tribute()
    district.add_tribute(tribute)
    assert tribute in district.tributes


def test_add_tribute_invalid():
    district = District()
    tribute = "Isn't a tribute"
    with pytest.raises(ValueError):
        district.add_tribute(tribute)


def test_remove_tribute():
    district = District()
    t1 = Tribute()
    district.cant_tributes = 0
    district.add_tribute(t1)
    assert len(district.tributes) == 1
    district.remove_tribute(t1)
    assert len(district.tributes) == 0


def test_get_number_district():
    district = District()
    district.number_district = 1
    expect = district.number_district
    res = district.get_number_district()
    assert expect == res


def test_get_cant_tribute():
    district = District()
    district.cant_tributes = 4
    expect = district.cant_tributes
    res = district.get_cant_tribute()
    assert expect == res
