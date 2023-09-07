from flask import url_for
from behave import given, when, then, step

# escenario 1
@given("que un tributo se encuentra en la posición (0, 3)")
def step_impl(context):
    pass

@when("el tributo tenga que moverse")
def step_impl(context):
    pass

@then("se moverá hacia abajo a la posición (1, 3)")
def step_impl(context):
    pass

# escenario 2
@given("que un tributo se encuentra en la posición (3, 0)")
def step_impl(context):
    pass

@when("el tributo se mueva")
def step_impl(context):
    pass

@then("se moverá hacia la derecha a la posición (3, 1)")
def step_impl(context):
    pass

# escenario 3
@given("que un tributo se encuentra en la posición (0, 0)")
def step_impl(context):
    pass

@when("el tributo tenga que avanzar")
def step_impl(context):
    pass

@then("avanzará en diagonal hacia la posición (1, 1)")
def step_impl(context):
    pass

# escenario 4
@given("que un tributo se encuentra en la posición (3, 2)")
def step_impl(context):
    pass

@when("el tributo avance")
def step_impl(context):
    pass

@then("avanzará hacia arriba a la posición (2, 2)")
def step_impl(context):
    pass

# escenario 5
@given("que un tributo se encuentra en la posición (0, 2)")
def step_impl(context):
    pass

@when("cuando realice un movimiento")
def step_impl(context):
    pass

@then("se moverá hacia la izquierda a la posición (0, 1)")
def step_impl(context):
    pass

# escenario 6
@given("que un tributo se encuentre en la posición (2, 1)")
def step_impl(context):
    pass

@step("no es adyacente a otro tributo")
def step_impl(context):
    pass

@step("no se encuentra en la misma celda que un ítem")
def step_impl(context):
    pass

@when("se ejecute un paso de iteración")
def step_impl(context):
    pass

@then("se moverá a una celda adyacente disponible (1, 1)")
def step_impl(context):
    pass