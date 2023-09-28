import pytest

from game.logic.district import District

# tests para metodo cset_config(...) 

def test_set_config_invalid_life():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(39, 5, 10, 2, 4) # life 39


def test_set_config_invalid_force():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(50, 100, 1, 3, 4) # force 100


def test_set_config_invalid_alliance():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(50, 10, 11, 3, 4) # aliance 11


def test_set_config_invalid_district():
    district = District()
    with pytest.raises(ValueError):
        district.set_config(50, 5, 10, 1000, 4) # district 1000 


@pytest.mark.parametrize("cant_tribute", [4, 5, 6]) # test parametrizado, la funcion se ejecuta tres veces, con 4, con 5 y con 6.
def test_set_config_valid_cant_tribute(cant_tribute):
    district = District()
    district.set_config(50, 6, 8, 2, cant_tribute)
    assert len(district.tributes) == cant_tribute # Por defecto la cantidad de tributos es 4, pero podrian agregarse 1 o 2 mas