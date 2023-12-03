import pytest
from app import create_app, db
from flask_jwt_extended import create_access_token
from game.logic.game_logic import GameLogic

@pytest.fixture
def app():
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        app.config['TESTING'] = True
        app.config['JWT_SECRET_KEY'] = 'clave_secreta_de_prueba'
        yield app
        db.session.remove()
        db.drop_all()    

@pytest.fixture
def client(app):
    return app.test_client()

invalid_inputs = [
    (101, 5, 3, 4, 0, 400),  # Invalid life
    (50, 4, 3, 4, 0, 400),  # Invalid force
    (50, 5, 2, 4, 0, 400),  # Invalid alliance
    (50, 5, 3, 3, 0, 400),  # Invalid cant_tributes
    (50, 5, 3, 4, -1, 400),  # Invalid cowardice
    (99.5, 5.5, 3, 4, 0, 400),  # Invalid sum of points
]

@pytest.mark.parametrize(
    "life, force, alliance, cant_tributes, cowardice, expected_status",
    invalid_inputs
)
def test_config_district_post_invalid_input(client, life, force, alliance, cant_tributes, cowardice, expected_status):
    access_token = create_access_token(identity=1)
    
    response = client.post('/game/district', json={
        "life": life,
        "force": force,
        "alliance": alliance,
        "cant_tributes": cant_tributes,
        "cowardice": cowardice
    },
    headers={'Authorization': f'Bearer {access_token}'})
    
    assert response.status_code == expected_status

def test_config_district_get(client):
    response = client.get('/game/district')
    assert response.status_code == 200

def test_config_district_post(client):
    access_token = create_access_token(identity=1)
    
    response = client.post('/game/district', json={
      "life":95,
      "force":5,
      "alliance":3,
      "cant_tributes":4,
      "cowardice":1
    },
    headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    
def test_game_put(client):
    access_token = create_access_token(identity=1)
    
    response = client.post('/game/district', json={
      "life":100,
      "force":5,
      "alliance":3,
      "cant_tributes":4,
      "cowardice":0
    },
    headers={'Authorization': f'Bearer {access_token}'})

    response = client.put(f'/game/{1}')
    assert response.status_code == 200
    

def test_game_get(client):
    access_token = create_access_token(identity=1)
    
    response = client.post('/game/district', json={
      "life":100,
      "force":5,
      "alliance":3,
      "cant_tributes":4,
      "cowardice":0
    },
    headers={'Authorization': f'Bearer {access_token}'})

    response = client.get(f'/game/{1}')
    assert response.status_code == 200
