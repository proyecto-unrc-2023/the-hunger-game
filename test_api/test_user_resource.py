import pytest
from app import create_app, db
from flask_jwt_extended import JWTManager
from user.user import User


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



def test_get_id(client):
    response = client.post("/game/get_id", json={
        "name":"manu"
    })
    assert response.json["error"] == 'Usuario no encontrado.'
    assert response.status_code == 404
    user = User()
    user.add_user('manu', 'RayoDeSol')
    response = client.post("/game/get_id", json={
        "name":"manu"
    })
    assert response.json["user_id"] == 1
    assert response.status_code == 200
    
def test_register(client):
    response = client.post("/game/get_id", json={
        "name":"manu"
    })
    assert response.json["error"] == 'Usuario no encontrado.'
    assert response.status_code == 404
    register = client.post("/game/register", json={
     "name":"manu",
     "password":"RayoDeSol"   
    })
    assert register.status_code == 200
    
    register2 = client.post("/game/register", json={
     "name":"manu",
     "password":"RayoDeSol2"   
    })
    assert register2.status_code == 400
    
def test_login_logout(client):
    register = client.post("/game/register", json={
        "name": "manu",
        "password": "RayoDeSol"   
    })
    
    login = client.post("/game/login", json={
        "name": "manu",
        "password": "RayoDeSol"
    })    
    assert login.status_code == 200
    
    access_token = login.json['access_token']
    
    logout = client.post("/game/logout", headers={'Authorization': f'Bearer {access_token}'})
    assert logout.status_code == 200


def test_userget(client):
    response = client.post("/game/get_user", json={
        "name":"manu"
    })
    assert response.json["error"] == 'Usuario no encontrado.'
    assert response.status_code == 404
    user = User()
    user.add_user('manu', 'RayoDeSol')
    response = client.post("/game/get_user", json={
        "name":"manu"
    })
    assert response.status_code == 200
    
def test_select_pj(client):
    user = User()
    user.add_user('manu', 'RayoDeSol')
    response = client.post("/game/select", json={
        "name":"manu",
        "pj":3
    })
    assert response.status_code == 200
    