from behave import given, when, then

from game.logic.game_logic import GameLogic


@given(u'que el juego se creo')
def step_impl(context):
    context.game = GameLogic()


@when(u'esta por comenzar la simulacion')
def step_impl(context):
    context.game.prepare_the_game(10, 10)


@then(u'no hay más de un tributo por celda')
def step_impl(context):
    tributes_with_same_pos = False
    all_tributes = []
    for m in range(6):
        for n in range(4):
            all_tributes.append(context.game.districts[m].tributes[n])
    cant_tributes = all_tributes.__len__()
    for i in range(10):
        for j in range(10):
            tribute_with_position = (i, j)
            counter = 0
            for k in range(cant_tributes):
                if (all_tributes[k]).pos == tribute_with_position:
                    counter += 1
        if counter > 1:
            tributes_with_same_pos = True

    assert tributes_with_same_pos is False


@then(u'dos tributos del mismo distrito deben tener las mismas caracteristicas')
def step_impl(context):
    tribute_zero = context.game.districts[0].tributes[0]
    tribute_one = context.game.districts[0].tributes[1]
    assert tribute_zero.force == tribute_one.force
    assert tribute_zero.life == tribute_one.life
    assert tribute_zero.alliance == tribute_one.alliance
    assert tribute_zero.max_life == tribute_one.max_life
    assert tribute_zero.district == tribute_one.district
    assert tribute_zero.cowardice == tribute_one.cowardice

@then(u'todos los distritos tienen al menos un tributo')
def step_impl(context):
    assert context.game.districts[0].cant_tributes > 0
    assert context.game.districts[1].cant_tributes > 0
    assert context.game.districts[2].cant_tributes > 0
    assert context.game.districts[3].cant_tributes > 0
    assert context.game.districts[4].cant_tributes > 0
    assert context.game.districts[5].cant_tributes > 0
