from behave import given, when, then

from game.logic.district import District
from game.logic.game_logic import GameLogic
from game.logic.tribute import Tribute


@given(u'que un juego fue creado')
def step_impl(context):
    context.game = GameLogic()
    context.game.new_game(4, 4)
    context.t0 = Tribute()
    context.d0 = District()
    context.t0.set_config_parameters(50, 8, 2, 0)
    context.d0.add_tribute(context.t0)
    context.game.districts.append(context.d0)


@given(u'que tributo se encuentra en la posición {f:d} {c:d}')
def step_impl(context, f, c):
    context.game.board.put_tribute(f, c, context.t0)
    assert context.t0.pos == (f, c)


@when(u'se mueve hacia "{direccion}"')
def step_impl(context, direccion):
    pass


@then(u'tributo se mueve hacia la posición {res1:d} {res2:d}')
def step_impl(context, res1, res2):
    context.t0.move_to(res1, res2, context.game.board)
    assert context.t0.pos == (res1, res2)