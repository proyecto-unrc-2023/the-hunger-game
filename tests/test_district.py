import pytest

from game.logic.district import District
from game.logic.tribute import Tribute


def test_set_config_invalid_life():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(-1, 8, 3, 6, 4)  # life -1


def test_set_config_invalid_force():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(50, 4, 1, 3, 4)  # force 4


def test_set_config_invalid_alliance():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(50, 20, 11, 3, 4)  # aliance 11


def test_set_config_tributes():
    district = District()
    district.set_config(50, 10, 6, 0, 5)
    list_tributes = district.tributes
    for i in range(len(list_tributes)):
        assert list_tributes[i].life == 50
        assert list_tributes[i].force == 10
        assert list_tributes[i].alliance == 6
        assert list_tributes[i].district == 0


def test_set_config_random_tributes():
    district = District()
    district.set_config_random(3) # 3 is number_district
    random_tributes = district.tributes
    for i in range(len(random_tributes)):
        assert random_tributes[i].life == 50
        assert 5 <= random_tributes[i].force <= 10
        assert 3 <= random_tributes[i].alliance <= 10
        assert random_tributes[i].district == 3

# tests for add and remove tribute

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


def test_remove_tribute_invalid():
    district = District()
    tribute = "Isn't a tribute"
    with pytest.raises(ValueError):
        district.remove_tribute(tribute)
        

def test_remove_tribute():
    district = District()
    t1 = Tribute()
    district.cant_tributes = 0
    district.add_tribute(t1)
    assert len(district.tributes) == 1
    district.remove_tribute(t1)
    assert len(district.tributes) == 0

# tests for getters()

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


# tests for buy_tribute(..)

def test_buy_tribute_points_less_than_4():
    district = District()
    district.set_config_by_default(0)
    points = 3
    with pytest.raises(ValueError):
        district.buy_tribute(district.tributes[0], points)

 
def test_buy_one_tribute():
    district = District()
    district.set_config_by_default(5)
    points = 10
    curr_points = district.buy_tribute(district.tributes[0], points)
    assert curr_points == points - 4
    assert len(district.tributes) == 5


def test_buy_two_tributes():
    district = District()
    district.set_config_by_default(3)
    points = 10
    curr_points = district.buy_tribute(district.tributes[0], points)
    assert curr_points == 6
    assert len(district.tributes) == 5
    
    curr_points = district.buy_tribute(district.tributes[0], curr_points)
    assert curr_points == 2
    assert len(district.tributes) == 6