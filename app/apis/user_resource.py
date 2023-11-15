from flask_restful import Resource
from app import db 
from user.user import User, UserSchema
from flask import jsonify, request
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token


class Structure(Resource):
        def get(self):
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            table_info = {}

            for table in tables:
                columns = inspector.get_columns(table)
                column_names = [column['name'] for column in columns]
                table_info[table] = column_names

            return jsonify(table_info)
        
class Register(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')  # Obtén el nombre de usuario desde los datos
        password = data.get('password')  # Obtén la contraseña desde los datos
        
        if name is None or password is None or name == '' or password == '':
            return {'message': 'Nombre de usuario y contraseña son obligatorios.'}, 400
        else:
            user = User()
            try:
                user.add_user(name, password)
                return {'message': 'Usuario registrado con éxito.'}, 200
            except IntegrityError as integrity_error:
                #si el username ya existe se captura la excepcion de integridad
                db.session.rollback() #se revierte la transaccion
                return {'error': 'El nombre de usuario ya esta en uso.'}, 400

class Login(Resource):
    def post(self):
        data = request.get_json()  
        user = User.query.filter_by(username=data['name'], password=data['password']).first()

        if user:
            #si el usuario existe entonces se inicia sesion
            access_token = create_access_token(identity=user.id) #se crea un token unico de acceso
            return {'message': 'Inicio de sesión exitoso.','access_token': access_token}, 200
        else:
            return {'error': 'Nombre de usuario o constraseña inválidos.'}, 400

class UserGet(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        
        if user:
            return user.json(), 200
        else:
            return {'error': 'Usuario no encontrado.'}, 404
        
class SelectPj(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        user.select_character(num_pj=data['pj'])
        

class UserIdGet(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        
        if user:
            result =user.get_id()
            response = {'user_id': result}
            return response, 200
        else:
            return {'error': 'Usuario no encontrado.'}, 404
        