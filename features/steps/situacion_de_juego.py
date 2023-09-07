from flask import url_for
from behave import given, when, then

@given('que empezo la simulacion')
def step_impl(context):
    pass

@given('un tributo es adyacente a otr')
def step_impl(context):
    pass


@given('esta sobre un item')
def step_impl(context):
    pass


@when('se ejecute un paso de iteracion')
def step_impl(context):
    pass


@then('el que no esta sobre el item, golpeara al otro')
def step_impl(context):
    pass


@then('el otro recoge el item, perdiendo asi una iteracion')
def step_impl(context):
    pass


@then('luego lucharan')
def step_impl(context):
    pass



@given('dos tributos enemigos son adyacentes')
def step_impl(context):
    pass


@given('estan luchando')
def step_impl(context):
    pass


@when('otro tributo visualize a los tributos luchando mediante su rango de vision')
def step_impl(context):
    pass


@when('sea adyacente a ambos')
def step_impl(context):
    pass


@then('le pegara al tributo que tenga mas vida')
def step_impl(context):
    pass


@given('dos tributos de distinto distritos son adyacentes')
def step_impl(context):
    pass


@when('llegue un tributo aliado de algunos de los dos tributos que estan luchando')
def step_impl(context):
    pass


@when('ambos tributos entran en el rango de vision del aliado')
def step_impl(context):
    pass


@then('el aliado atacara al tributo enemigo')
def step_impl(context):
    pass


@given('que dos tributos son de distintos distritos')
def step_impl(context):
    pass


@given('tienen la mismas caracteristicas')
def step_impl(context):
    pass


@given('tienen la misma cantidad de vida')
def step_impl(context):
    pass


@when('se encuentran y enfrentan en el mapa')
def step_impl(context):
    pass


@then('ambos tributos mueren')
def step_impl(context):
    pass


@given('que un tributo pertenece a un distrito y otro es neurtro')
def step_impl(context):
    pass


@when('se encuentran en el mapa')
def step_impl(context):
    pass


@when('el tributo perteneciente al distrito es capaz de aliarse')
def step_impl(context):
    pass


@then('el tributo neutro se convierte en un miembro del tributo que se encontro')
def step_impl(context):
    pass


@then('adquiere las caracteristicas del distrito al cual corresponde')
def step_impl(context):
    pass


@given('un tributo que pertenece a un distrito y otro neutro')
def step_impl(context):
    pass


@when('ambos tributos se encuentran en el mapa')
def step_impl(context):
    pass


@when('el tributo del distrito NO es capaz de aliarse')
def step_impl(context):
    pass


@then('el tributo del distrito lucha con el tributo neutro')
def step_impl(context):
    pass


@given('dos tributos')
def step_impl(context):
    pass


@when('ambos pertenecen al mismo distrito')
def step_impl(context):
    pass


@then('se ignoran')
def step_impl(context):
    pass


@given('que dos tributos son de distinto distrito')
def step_impl(context):
    pass


@given('tienen distintas estadisticas')
def step_impl(context):
    pass


@when('luchan')
def step_impl(context):
    pass


@then('uno de ellos muere')
def step_impl(context):
    pass


@given('que dos tributos son neutros')
def step_impl(context):
    pass


@given('que un tributo encuentra un item de curacion en el mapa')
def step_impl(context):
    pass


@given('no tenga la vida al maximo')
def step_impl(context):
    pass


@when('el tributo se encuentra sobre el item')
def step_impl(context):
    pass


@then('su vida incrementa')
def step_impl(context):
    pass


@then('el item desaparece del mapa')
def step_impl(context):
    pass


@given('tiene la vida al maximo')
def step_impl(context):
    pass


@when('se encuentra sobre el item')
def step_impl(context):
    pass


@then('lo ignora')
def step_impl(context):
    pass


@given('que un tributo encuentra una espada en el mapa')
def step_impl(context):
    pass


@when('el tributo no tenga una espada')
def step_impl(context):
    pass


@when('se escuentre sobre la espada')
def step_impl(context):
    pass


@then('su daño se incrementa')
def step_impl(context):
    pass


@then('la espada desaparece del mapa')
def step_impl(context):
    pass


@when('el tributo tenga una espada')
def step_impl(context):
    pass


@when('se encuentre sobre la espada')
def step_impl(context):
    pass


@then('no la recoge')
def step_impl(context):
    pass


@when('se cruzan en el mapa')
def step_impl(context):
    pass


@then('el tributo con más fuerza inflige más daño')
def step_impl(context):
    pass


@then('el tributo con menos fuerza inflige menos daño')
def step_impl(context):
    pass
