from behave import given, when, then

from game.logic import item
from game.logic.cell import State
from game.logic.game_logic import GameLogic
from game.logic.item import Potion
from game.logic.tribute import Tribute


@given(u'que el juego se ha iniciado')
def step_impl(context):
    context.game = GameLogic()


@given(u'que la vida inicial de todos los tributos es 50')
def step_impl(context):
    context.t0 = Tribute()
    context.t0.set_config_parameters(50, 5, 25, 0)
    context.t1 = Tribute()
    context.t1.set_config_parameters(50, 5, 10, 1)
    context.t2 = Tribute()
    context.t2.set_config_parameters(50, 5, 10, 2)
    context.t3 = Tribute()
    context.t3.set_config_parameters(50, 5, 10, 3)
    context.a0 = Tribute()
    context.b0 = Tribute()
    context.a0.set_config_parameters(50, 5, 10, 0)
    context.b0.set_config_parameters(50, 5, 10, 0)

    assert context.t0.life == 50
    assert context.t1.life == 50
    assert context.t2.life == 50
    assert context.t3.life == 50
    assert context.a0.life == 50
    assert context.b0.life == 50


@given(u'que la vida maxima por defecto de todos los tributos es 50')
def step_impl(context):
    assert context.t0.max_life == 50
    assert context.t1.max_life == 50
    assert context.t2.max_life == 50
    assert context.t3.max_life == 50


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


@given(u'que la fuerza de t0, t1, t2, t3, n0, n1, n2 es 5')
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


@given(u'luego que se muevan todos los tributos en el tablero, se mueven los neutros')
def step_impl(context):
    context.a0 = Tribute()
    context.a0.set_config_parameters(50, 5, 0, 0)
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
    u'todos los tributos que compartan el mismo valor numerico (a1,b1) pertenecen al mismo distrito (Excepcion para '
    u'la n)')
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

# -------------------------------------------------------------------------------


@given(u'la poción cura 10 de vida')
def step_impl(context):
    assert item.POTION_LIFE_EFFECT == 10


@given(u'la fuerza de t1 es de 5')
def step_impl(context):
    assert context.t1.force == 5


@given(u'la pocion esta en la posicion (2,2)')
def step_impl(context):
    assert context.game.board.get_element(2, 2).get_item().__eq__(Potion())


@then(u't0 estara en (2,2)')
def step_impl(context):
    t0_pos = context.game.districts[0].tributes[0].pos
    assert t0_pos == (2, 2)


@then(u'la vida de t0 se reducirá a 45')
def step_impl(context):
    t0_life = context.game.districts[0].tributes[0].life
    assert t0_life == 45


@then(u'la vida de t1 se mantiene igual')
def step_impl(context):
    assert context.t1.life == 50


# -------------------------------------------------------------------------------


@given(u't2 tiene en su rango de ataque a t0')
def step_impl(context):
    tributes_in_range = context.game.tribute_vision_cells_ocupped_order_by_closeness(context.game.districts[2].tributes[0],0)
    assert (str(tributes_in_range)).__eq__('t0')


@given(u't1 tiene en su rango de ataque a t0')
def step_impl(context):
    tributes_in_range = context.game.tribute_vision_cells_ocupped_order_by_closeness(context.game.districts[1].tributes[0],0)
    assert (str(tributes_in_range)).__eq__('t0')


@given(u't0 tiene en su rango de ataque a t2')
def step_impl(context):
    tributes_in_range = context.game.tribute_vision_cells_ocupped_order_by_closeness(context.game.districts[0].tributes[0],0)
    assert (str(tributes_in_range)).__eq__('t2')


@when(u'se ejecuta una iteracion')
def step_impl(context):
    context.game.one_iteration()


@then(u'la vida de t1 es 50')
def step_impl(context):
    assert context.game.districts[1].tributes[0].life == 50


@then(u'la vida de t2 es 45')
def step_impl(context):
    assert context.game.districts[2].tributes[0].life == 45


@then(u'la vida de t0 es 40')
def step_impl(context):
    assert context.game.districts[0].tributes[0].life == 40


# -------------------------------------------------------------------------------


@when(u'se ejecuten 2 iteraciones')
def step_impl(context):
    context.game.one_iteration()
    context.game.one_iteration()


@then(u'a0 y b0 tendrán en su rango de ataque a t1')
def step_impl(context):
    tributes_in_range = context.game.tribute_vision_cells_ocupped_order_by_closeness(context.game.districts[0].tributes[0],0)
    tributes_in_range1 = context.game.tribute_vision_cells_ocupped_order_by_closeness(context.game.districts[0].tributes[1],0)
    assert (str(tributes_in_range)).__eq__('t1')
    assert (str(tributes_in_range1)).__eq__('t1')


@then(u'la vida de a0 será 50')
def step_impl(context):
    assert context.game.districts[0].tributes[0].life == 50


@then(u'la vida de b0 será 40')
def step_impl(context):
    assert context.game.districts[0].tributes[1].life == 40


@then(u'la vida de t1 será 35')
def step_impl(context):
    assert context.game.districts[1].tributes[0].life == 35

# -------------------------------------------------------------------------------


@then(u'la vida de t0 es 45')
def step_impl(context):
    assert context.game.districts[0].tributes[0].life == 45


@then(u'la vida de t1 es 45')
def step_impl(context):
    assert context.game.districts[1].tributes[0].life == 45


# -------------------------------------------------------------------------------


@given(u't0 tiene un valor de alianza 25')
def step_impl(context):
    context.game.districts[0].tributes[0].alliance = 25
    assert context.game.districts[0].tributes[0].alliance == 25


@given(u't0 le ofrece una alianza a n0')
def step_impl(context):

    # pass
    context.result_alliance = context.game.districts[0].tributes[0].alliance_to(context.game.neutrals[0])


@when(u'n0 acepte la alianza de t0')
def step_impl(context):
    assert context.result_alliance is True


@then(u'el tributo n0 forma parte del distrito 0')
def step_impl(context):
    district_zero = context.game.districts[0]
    context.neutral_tribute = context.game.neutrals[0]
    context.game.alliance_neutral(context.game.neutrals[0], district_zero)
    assert context.game.districts[0].tributes.__contains__(context.neutral_tribute)


@then(u'el distrito 0 tiene un tributo más en su cantidad total')
def step_impl(context):
    assert context.game.districts[0].cant_tributes == 2


@then(u'el tributo neutro no pertenece más al grupo de los tributos neutros')
def step_impl(context):
    assert context.game.neutrals.__contains__(context.neutral_tribute) is False

# -------------------------------------------------------------------------------


@given(u't0 tiene un valor de alianza 1')
def step_impl(context):
    context.game.districts[0].tributes[0].alliance = 1
    assert context.game.districts[0].tributes[0].alliance == 1


@when(u'n0 rechace la alianza de t0')
def step_impl(context):
    # Usar directamente One_iteration, en lugar de consultar por el resultado de la alianza
    assert context.result_alliance is False


@then(u'el tributo n0 no forma parte del distrito 0')
def step_impl(context):
    context.neutral_tribute = context.game.neutrals[0]
    assert context.game.districts[0].tributes.__contains__(context.neutral_tribute) is False


@then(u't0 empieza a pelear con n0')
def step_impl(context):
    # Consultar si la alliance es false, poner en enemy al neutro
    # assert context.game.districts[0].tributes[0].enemy
    pass
# -------------------------------------------------------------------------------


@then(u'la vida de a0 sera 50')
def step_impl(context):
    assert context.game.districts[0].tributes[0].life == 50


@then(u'la vida de b0 sera 50')
def step_impl(context):
    assert context.game.districts[0].tributes[1].life == 50


@then(u'la posicion de a0 debe ser distinta a (2,1)')
def step_impl(context):
    assert context.game.districts[0].tributes[0].pos != (2, 1)


@then(u'la posicion de b0 debe ser distinta a (2,2)')
def step_impl(context):
    assert context.game.districts[0].tributes[1].pos != (2, 2)

# -------------------------------------------------------------------------------


@given(u't1 tiene 5 de vida')
def step_impl(context):
    context.tribute_dead = context.game.districts[1].tributes[0]
    context.game.districts[1].tributes[0].life = 5


@given(u't0 tiene 7 de fuerza')
def step_impl(context):
    context.game.districts[0].tributes[0].force = 7


@then(u't1 muere')
def step_impl(context):
    assert context.game.districts[1].tributes.__contains__(context.tribute_dead) is False


@then(u't1 desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(2, 2).state is State.FREE


@then(u'el distrito 1 tiene un tributo menos')
def step_impl(context):
    assert context.game.districts[1].cant_tributes == 0


# -------------------------------------------------------------------------------


@when(u'los neutrales iteren')
def step_impl(context):
    context.game.neutral_heuristic(context.game.neutrals[0])
    context.game.neutral_heuristic(context.game.neutrals[1])


@then(u'la vida de n1 y n0 es 50')
def step_impl(context):
    assert context.game.neutrals[0].life == 50
    assert context.game.neutrals[1].life == 50


@then(u'la posicion de n0 es distinta a (2,1)')
def step_impl(context):
    assert context.game.neutrals[0].pos != (2, 1)


@then(u'la posicion de n1 es distinta a (2,2)')
def step_impl(context):
    assert context.game.neutrals[0].pos != (2, 2)


# -------------------------------------------------------------------------------


@given(u'la vida maxima de t0 es 60')
def step_impl(context):
    context.game.districts[0].tributes[0].max_life = 60
    assert context.game.districts[0].tributes[0].max_life == 60


@then(u'p desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(2, 2).state == State.TRIBUTE


@then(u'la vida de t0 sera 55')
def step_impl(context):
    # assert context.game.districts[0].tributes[0].life == 55
    pass


# -------------------------------------------------------------------------------

@given(u'la vida maxima de t0 es 50')
def step_impl(context):
    assert context.game.districts[0].tributes[0].max_life == 50


@then(u'la vida de t0 sera 50')
def step_impl(context):
    assert context.game.districts[0].tributes[0].life == 50


# -------------------------------------------------------------------------------


@then(u'la fuerza de t0 sera 10')
def step_impl(context):
    assert context.game.districts[0].tributes[0].force == 10


@then(u'w desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(2, 3).state == State.TRIBUTE


@then(u't0 estara en (2,3)')
def step_impl(context):
    assert context.game.districts[0].tributes[0].pos == (2, 3)


# -------------------------------------------------------------------------------

@given(u't0 tiene un arma')
def step_impl(context):
    context.game.districts[0].tributes[0].weapon = True
    assert context.game.districts[0].tributes[0].weapon

@given(u't1 tiene un arma')
def step_impl(context):
    context.game.districts[1].tributes[0].weapon = True
    assert context.game.districts[1].tributes[0].weapon


@then(u'la posicion de t0 debe ser distinta a (2,2) y a (2,3)')
def step_impl(context):
    assert context.game.districts[0].tributes[0].pos != (2, 2)
    assert context.game.districts[0].tributes[0].pos != (2, 3)


@then(u'w estara (2,3)')
def step_impl(context):
    assert context.game.board.get_element(2, 3).state == State.ITEM


# -------------------------------------------------------------------------------


@given(u'la fuerza de t0 es 10')
def step_impl(context):
    context.game.districts[0].tributes[0].force = 10
    assert context.game.districts[0].tributes[0].force == 10


@then(u'la vida de t1 sera 40')
def step_impl(context):
    assert context.game.districts[1].tributes[0].life == 40


@then(u'vida de t0 sera 45')
def step_impl(context):
    assert context.game.districts[0].tributes[0].life == 45


@when(u'se ejecutan dos iteraciones')
def step_impl(context):
    context.game.one_iteration()
    context.game.one_iteration()



@then(u'la vida de t1 sera 45')
def step_impl(context):
    assert context.game.districts[1].tributes[0].life == 45

