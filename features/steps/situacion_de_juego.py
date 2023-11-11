from behave import given, when, then

from game.logic import item
from game.logic.cell import State
from game.logic.game_logic import GameLogic
from game.logic.item import PotionLife, Weapon
from game.logic.tribute import Tribute


# BACKGROUND


@given(u'que el juego se ha creado')
def step_impl(context):
    context.game = GameLogic()


@given(u'que la vida inicial de todos los tributos es 50')
def step_impl(context):
    context.t0 = Tribute()
    context.t0.set_config_parameters(50, 5, 25, 0, 0)
    context.t1 = Tribute()
    context.t1.set_config_parameters(50, 5, 10, 1, 0)
    context.t2 = Tribute()
    context.t2.set_config_parameters(50, 5, 10, 2, 0)
    context.t3 = Tribute()
    context.t3.set_config_parameters(50, 5, 10, 3, 0)
    context.a0 = Tribute()
    context.b0 = Tribute()
    context.a0.set_config_parameters(50, 5, 10, 0, 0)
    context.b0.set_config_parameters(50, 5, 10, 0, 0)


@given(u'que la vida maxima por defecto de todos los tributos es 50')
def step_impl(context):
    assert context.t0.max_life == 50
    assert context.t1.max_life == 50
    assert context.t2.max_life == 50
    assert context.t3.max_life == 50
    assert context.a0.max_life == 50
    assert context.b0.max_life == 50


@given(u'que la vida de n0, n1, n2 es 50 y no pertenecen a ningun distrito')
def step_impl(context):
    context.n0 = Tribute()
    context.n0.life = 50
    context.n1 = Tribute()
    context.n1.life = 50
    context.n2 = Tribute()
    context.n2.life = 50
    assert context.n0.life == 50
    assert context.n1.life == 50
    assert context.n2.life == 50


@given(u'que la fuerza de todos los tributos es 5')
def step_impl(context):
    context.n0.force = 5
    context.n1.force = 5
    context.n2.force = 5
    assert context.t0.force == 5
    assert context.t1.force == 5
    assert context.t2.force == 5
    assert context.t3.force == 5
    assert context.n0.force == 5
    assert context.n1.force == 5
    assert context.n2.force == 5
    assert context.a0.force == 5
    assert context.b0.force == 5


@given(u'luego que se muevan todos los tributos en el tablero, se mueven los neutros')
def step_impl(context):
    context.a0 = Tribute()
    context.a0.set_config_parameters(50, 5, 0, 0, 0)
    context.game1 = GameLogic()
    context.game1.new_game(3, 3)
    context.game1.put_tribute(1, 1, context.a0)
    context.game1.put_neutral(2, 2)
    context.game1.one_iteration()
    context.n5 = context.game1.neutrals[0]
    assert context.n5.enemy == context.a0
    assert context.a0.life == 45
    assert context.n5.life == 50


@given(
    u'todos los tributos que compartan el mismo valor numerico (por ejemplo a1,b1) pertenecen al mismo distrito ('
    u'Excepcion para la n)')
def step_impl(context):
    context.expected = '  |n0|t1\n' \
                       'a1|b0|a0\n' \
                       'a2|n1|b2'
    context.game2 = GameLogic()
    context.game2.from_string(context.expected)
    context.district0 = context.game2.districts[0]
    assert context.district0.tributes[0].district == 0
    assert context.district0.tributes[1].district == 0


@given(u'que el tablero de juego es el siguiente')
def step_impl(context):
    string = context.game.table_to_string(context.table)
    context.game.from_string(string)


@when(u'se ejecuta una iteracion')
def step_impl(context):
    context.game.one_iteration()


@given(u'la poción cura 10 de vida')
def step_impl(context):
    assert item.POTION_LIFE_EFFECT == 10


@given(u'la pocion esta en la posicion (2,2)')
def step_impl(context):
    assert context.game.get_item_pos(2, 2).__eq__(PotionLife())


@given(u'{a} tiene en su rango de ataque a {b}')
def step_impl(context, a, b):
    tributes_in_range = context.game.tribute_vision_closeness(context.game.get_tribute_by_name(a))
    assert (str(tributes_in_range)).__eq__(b)


@then(u'{a} tiene vida {v0:d}')
def step_impl(context, a, v0):
    neutral_or_not = a[0]
    if neutral_or_not == 'n':
        assert context.game.get_neutral_by_name(a).life == v0
    else:
        if context.game.get_tribute_by_name(a) is None:
            assert v0 == 0
        else:
            assert context.game.get_tribute_by_name(a).life == v0


@given(u'la vida de {b} es {v2:d}')
def step_impl(context, b, v2):
    context.game.get_tribute_by_name(b).life = v2


@given(u'la vida de {a} es {v3:d}')
def step_impl(context, a, v3):
    context.game.get_tribute_by_name(a).life = v3


@then(u'{b} tiene vida {v1:d}')
def step_impl(context, b, v1):
    neutral_or_not = b[0]
    if neutral_or_not == 'n':
        assert context.game.get_neutral_by_name(b).life == v1
    else:
        if context.game.get_tribute_by_name(b) is None:
            assert v1 == 0
        else:
            assert context.game.get_tribute_by_name(b).life == v1


@then(u'{a} tiene el arma {g}')
def step_impl(context, a, g):
    context.weapon = Weapon.get_weapon_by_name(g)
    assert (context.weapon.__str__()).__eq__(g)
    assert context.weapon.get_weapon_range() == context.game.get_tribute_by_name(a).range


@given(u'{a} tiene el arma {g}')
def step_impl(context, a, g):
    context.item = Weapon.get_weapon_by_name(g)
    context.tribute = context.game.get_tribute_by_name(a)
    context.item.apply_effect(context.tribute)


@given(u'{a} tiene arma {state}')
def step_impl(context, a, state):
    if state == 'False':
        assert context.game.get_tribute_by_name(a).weapon is False
    else:
        context.game.get_tribute_by_name(a).weapon = True


@given(u'{a} tiene una vida maxima {mv0:d}')
def step_impl(context, a, mv0):
    context.game.get_tribute_by_name(a).max_life = mv0


@then(u'{a} tiene fuerza {f0:d}')
def step_impl(context, a, f0):
    assert context.game.get_tribute_by_name(a).force == f0


@then(u'el item {i} tiene un estado {status}')
def step_impl(context, i, status):
    pos = (1, 2)
    context.cell = context.game.get_cell(pos)
    if status == 'used':
        assert context.cell.get_state() is State.TRIBUTE
    else:
        assert context.cell.get_state() is State.ITEM


@given(u'{a} tiene un arco')
def step_impl(context, a):
    context.game.get_tribute_by_name(a).weapon = True
    context.game.get_tribute_by_name(a).range = 3
    context.game.get_tribute_by_name(a).force = 6


@given(u'{a} tiene una lanza')
def step_impl(context, a):
    context.game.get_tribute_by_name(a).weapon = True
    context.game.get_tribute_by_name(a).range = 2
    context.game.get_tribute_by_name(a).force = 8


@then(u'la vida de {a} es {l1:d}')
def step_impl(context, a, l1):
    assert context.game.get_tribute_by_name(a).life == l1


@then(u'{a} esta en la posicion {x:d} {y:d}')
def step_impl(context, a, x, y):
    assert context.game.get_tribute_by_name(a).pos == (x, y)


@then(u'{a} tiene en su rango de ataque a {b}')
def step_impl(context, a, b):
    tributes_in_range = context.game.tribute_vision_closeness(context.game.get_tribute_by_name(a))
    assert (str(tributes_in_range)).__eq__(b)


@then(u'{a} tiene un arma con rango {range:d}')
def step_impl(context, a, range):
    if range != 0:
        assert context.game.get_tribute_by_name(a).range == range
    else:
        pass


@given(u't0 y t1 no tienen arma')
def step_impl(context):
    assert context.game.get_tribute_by_name('t0').weapon is False
    assert context.game.get_tribute_by_name('t1').weapon is False


@given(u't0 tiene un punto de cobardia disponible')
def step_impl(context):
    context.game.get_tribute_by_name('t0').cowardice = 1
    assert context.game.get_tribute_by_name('t0').cowardice == 1


@then(u't0 usará medio punto de cobardia')
def step_impl(context):
    assert context.game.get_tribute_by_name('t0').cowardice == 0.5


@given(u'{b} tiene un valor de alianza {al1:d}')
def step_impl(context, b, al1):
    context.game.get_tribute_by_name(b).alliance = al1


@given(u'{b} le ofrece una alianza a {n}')
def step_impl(context, b, n):
    context.result_alliance = context.game.get_tribute_by_name(b).alliance_to(context.game.get_neutral_by_name(n))


@when(u'{n} decida el resultado de la alianza con el districto {d1:d}')
def step_impl(context, n, d1):
    if context.result_alliance:
        context.district = context.game.districts[d1]
        context.game.alliance_neutral(context.game.get_neutral_by_name(n),  context.district)
        context.result = 'accept'
    else:
        context.result = 'reject'


@then(u'el resultado es {alliance}')
def step_impl(context, alliance):
    assert context.result == alliance


@then(u'el distrito {d1:d} tiene {ct:d} tributos')
def step_impl(context, d1, ct):
    assert context.game.get_list_tributes(d1).__len__() == ct


@then(u'la cantidad de tributos neutros es {ctn:d}')
def step_impl(context, ctn):
    assert context.game.neutrals.__len__() == ctn


@then(u'la posicion de {a} debe ser distinta a (2,1)')
def step_impl(context, a):
    neutral_or_not = a[0]
    if neutral_or_not == 'n':
        assert context.game.get_neutral_by_name(a).pos != (2, 1)
    else:
        assert context.game.get_tribute_pos(a) != (2, 1)


@then(u'la posicion de {b} debe ser distinta a (2,2)')
def step_impl(context, b):
    neutral_or_not = b[0]
    if neutral_or_not == 'n':
        assert context.game.get_neutral_by_name(b).pos != (2, 2)
    else:
        assert context.game.get_tribute_pos(b) != (2, 2)


@given(u't1 tiene 5 de vida')
def step_impl(context):
    context.tribute_dead = context.game.get_tribute_by_name('t1')
    context.game.get_tribute_by_name('t1').life = 5


@given(u't0 tiene 7 de fuerza')
def step_impl(context):
    context.game.get_tribute_by_name('t0').force = 7


@then(u't1 muere')
def step_impl(context):
    assert context.game.get_list_tributes(1).__contains__(context.tribute_dead) is False


@then(u't1 desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(2, 2).state is State.FREE


@then(u'el distrito 1 tiene un tributo menos')
def step_impl(context):
    assert context.game.get_list_tributes(1).__len__() == 0


@given(u't0 tiene un arma')
def step_impl(context):
    context.game.get_tribute_by_name('t0').weapon = True
    assert context.game.get_tribute_by_name('t0').weapon


@given(u't1 tiene un arma')
def step_impl(context):
    context.game.get_tribute_by_name('t1').weapon = True
    assert context.game.get_tribute_by_name('t1').weapon


@then(u'w estara (2,3)')
def step_impl(context):
    assert context.game.board.get_element(2, 3).state == State.ITEM
