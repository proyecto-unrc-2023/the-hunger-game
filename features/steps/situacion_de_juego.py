from behave import given, when, then

from game.logic import item
from game.logic.cell import State
from game.logic.game_logic import GameLogic, GameMode
from game.logic.item import PotionLife
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


# -------------------------------------------------------------------------------
# DIFERENTES FORMAS DE ITERAR EL JUEGO


@when(u'se ejecuta una iteracion')
def step_impl(context):
    context.game.one_iteration()


@when(u'se ejecuten 2 iteraciones')
def step_impl(context):
    context.game.one_iteration()
    context.game.one_iteration()


@when(u'se ejecute el juego')
def step_impl(context):
    context.game.mode = GameMode.SIMULATION
    context.game.heuristic_of_game()


# -------------------------------------------------------------------------------
# Dos tributos luchan y uno de ellos encuentra un item de curacion


@given(u'la poción cura 10 de vida')
def step_impl(context):
    assert item.POTION_LIFE_EFFECT == 10  # pass


@given(u'la pocion esta en la posicion (2,2)')
def step_impl(context):
    assert context.game.get_item_pos(2, 2).__eq__(PotionLife())


# -------------------------------------------------------------------------------
# Tres tributos luchan


@given(u'{a} tiene en su rango de ataque a {b}')
def step_impl(context, a, b):
    tributes_in_range = context.game.tribute_vision_closeness(context.game.get_tribute_by_name(a))
    assert (str(tributes_in_range)).__eq__(b)


@then(u'la vida de {a} es {l1:d}')
def step_impl(context, a, l1):
    assert context.game.get_tribute_by_name(a).life == l1


@then(u'{a} esta en la posicion {x:d} {y:d}')
def step_impl(context, a, x, y):
    assert context.game.get_tribute_by_name(a).pos == (x, y)


# -------------------------------------------------------------------------------
# Dos tributos luchan y llega un aliado


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

# -------------------------------------------------------------------------------
# Enfrentamiento entre 2 tributos


@given(u't0 y t1 no tienen arma')
def step_impl(context):
    assert context.game.get_tribute_by_name('t0').weapon is False
    assert context.game.get_tribute_by_name('t1').weapon is False

# -------------------------------------------------------------------------------
# Un tributo huye de un combate


@given(u't0 tiene un punto de cobardia disponible')
def step_impl(context):
    context.game.get_tribute_by_name('t0').cowardice = 1
    assert context.game.get_tribute_by_name('t0').cowardice == 1


@then(u't0 usará medio punto de cobardia')
def step_impl(context):
    assert context.game.get_tribute_by_name('t0').cowardice == 0.5


# -------------------------------------------------------------------------------
# Tributo con mayor fuerza inflige mayor daño a otro tributo con menor fuerza en combate

@given(u'la fuerza de t0 es 10')
def step_impl(context):
    context.game.get_tribute_by_name('t0').force = 10
    assert context.game.get_tribute_by_name('t0').force == 10


# -------------------------------------------------------------------------------
# Se producen dos luchas al mismo tiempo


@then(u'el distrito 0 es el ganador')
def step_impl(context):
    assert context.game.game_ended()
    context.game.winner_district()
    assert context.game.winner == 0


# -------------------------------------------------------------------------------
# Dos tributos luchan a muerte y uno de ellos tiene un arco
# Dos tributos luchan a muerte y uno de ellos tiene una lanza
# Dos tributos luchan a muerte y uno de ellos tiene una espada


@given(u'la vida de t1 es 5')
def step_impl(context):
    context.game.get_tribute_by_name('t1').life = 5
    assert context.game.get_tribute_by_name('t1').life == 5


@then(u't1 esta muerto')
def step_impl(context):
    assert context.game.get_list_tributes(1).__len__() == 0


# -------------------------------------------------------------------------------
# Un tributo muere por el efecto de la pocion de veneno


@given(u'la vida de t0 es 5')
def step_impl(context):
    context.game.get_tribute_by_name('t0').life = 5
    assert context.game.get_tribute_by_name('t0').life == 5


@then(u't0 esta muerto')
def step_impl(context):
    assert context.game.get_list_tributes(0).__len__() == 0


# -------------------------------------------------------------------------------
# Un tributo se alia con un tributo neutro

@given(u't0 tiene un valor de alianza 25')
def step_impl(context):
    context.game.get_tribute_by_name('t0').alliance = 25
    assert context.game.get_tribute_by_name('t0').alliance == 25


@given(u't0 le ofrece una alianza a n0')
def step_impl(context):
    context.result_alliance = context.game.get_tribute_by_name('t0').alliance_to(context.game.get_neutral_by_name('n0'))


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
    assert context.game.get_list_tributes(0).__len__() == 2


@then(u'el tributo neutro no pertenece más al grupo de los tributos neutros')
def step_impl(context):
    assert context.game.neutrals.__contains__(context.neutral_tribute) is False


# -------------------------------------------------------------------------------
# Un tributo no logra aliarse con un tributo neutro y el tributo muere

@given(u't0 tiene un valor de alianza 1')
def step_impl(context):
    tribute_zero = context.game.get_tribute_by_name('t0')
    tribute_zero.alliance = 1
    assert tribute_zero.alliance == 1


@when(u'n0 rechace la alianza de t0')
def step_impl(context):
    assert context.result_alliance is False


@then(u'el tributo n0 no forma parte del distrito 0')
def step_impl(context):
    context.neutral_tribute = context.game.get_neutral_by_name('n0')
    assert context.game.get_list_tributes(0).__contains__(context.neutral_tribute) is False


@then(u't0 empieza a pelear con n0')
def step_impl(context):
    assert context.game.get_neutral_by_name('n0').enemy == context.game.get_tribute_by_name('t0')


# -------------------------------------------------------------------------------
# Dos tributos del mismo distrito se encuentran en el mapa y se ignoran


@then(u'la posicion de t0 debe ser distinta a (2,1)')
def step_impl(context):
    assert context.game.get_tribute_pos('t0') != (2, 1)


@then(u'la posicion de a0 debe ser distinta a (2,2)')
def step_impl(context):
    assert context.game.get_tribute_pos('t0') != (2, 2)


# -------------------------------------------------------------------------------
# Muerte de un tributo en batalla


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

# -------------------------------------------------------------------------------
# Dos tributos neutros se encuentran en el mapa y se ignoran


@when(u'los neutrales iteren')
def step_impl(context):
    context.game.neutral_heuristic(context.game.get_neutral_by_name('n0'))
    context.game.neutral_heuristic(context.game.get_neutral_by_name('n1'))


@then(u'la vida de neutros sigue igual')
def step_impl(context):
    assert context.game.get_neutral_by_name('n0').life == 50
    assert context.game.get_neutral_by_name('n1').life == 50


@then(u'la posicion de n0 es distinta a (2,1)')
def step_impl(context):
    assert context.game.get_neutral_by_name('n0').pos != (2, 1)


@then(u'la posicion de n1 es distinta a (2,2)')
def step_impl(context):
    assert context.game.get_neutral_by_name('n0').pos != (2, 2)


# -------------------------------------------------------------------------------
# Tributo encuentra un item de curacion y la utiliza

@given(u'la vida maxima de t0 es 60')
def step_impl(context):
    context.game.get_tribute_by_name('t0').max_life = 60
    assert context.game.get_tribute_by_name('t0').max_life == 60


@then(u'pl desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(3, 2).state != State.ITEM


# -------------------------------------------------------------------------------
# Tributo encuentra una pocion de curación y no le aplica su efecto

@given(u'la vida maxima de t0 es 50')
def step_impl(context):
    assert context.game.get_tribute_by_name('t0').max_life == 50


# -------------------------------------------------------------------------------
# Tributo encuentra una pocion de fuerza y la utiliza


@then(u'pf desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(3, 2).state != State.ITEM


@then(u'la fuerza de t0 es 10')
def step_impl(context):
    assert context.game.get_tribute_by_name('t0').force == 10


# -------------------------------------------------------------------------------
# Tributo encuentra una pocion de veneno y la utiliza


@then(u'po desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(3, 2).state != State.ITEM


# -------------------------------------------------------------------------------
# Tributo que no tiene arma encuentra una arma y la recoge

@then(u'w desaparece del mapa')
def step_impl(context):
    assert context.game.board.get_element(2, 3).state == State.TRIBUTE


# -------------------------------------------------------------------------------
# Tributo que tiene arma encuentra una arma y NO la recoge
# Tributo ignora el arma y pelea con otro tributo

@given(u't0 tiene un arma')
def step_impl(context):
    context.game.get_tribute_by_name('t0').weapon = True
    assert context.game.get_tribute_by_name('t0').weapon


@given(u't1 tiene un arma')
def step_impl(context):
    context.game.get_tribute_by_name('t1').weapon = True
    assert context.game.get_tribute_by_name('t1').weapon


@then(u'la posicion de t0 debe ser distinta a (2,2) y a (2,3)')
def step_impl(context):
    assert context.game.get_tribute_pos('t0') != (2, 2)
    assert context.game.get_tribute_pos('t0') != (2, 3)


@then(u'w estara (2,3)')
def step_impl(context):
    assert context.game.board.get_element(2, 3).state == State.ITEM
