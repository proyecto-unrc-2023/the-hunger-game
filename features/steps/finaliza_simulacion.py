from behave import given, when, then

from game.logic.game_logic import GameLogic


@given(u'que el tablero se encuentra en el siguiente estado')
def step_impl(context):
    context.game = GameLogic()
    string = context.game.table_to_string(context.table)
    context.game.from_string(string)


@when(u'se ejecute la ultima iteracion')
def step_impl(context):
    context.game.one_iteration()


@then(u'el unico distrito sobreviviente gana la partida')
def step_impl(context):
    context_district_winner = context.game.winner_district()
    assert context_district_winner == 0
