from flask_restful import Resource
from app import db 
from user.user import User, UserSchema
from flask import jsonify, request
from sqlalchemy import inspect

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
            return {'message': 'Nombre de usuario y contraseña son obligatorios'}, 400
        else:
            user = User()
            user.add_user(name, password)
            return {'message': 'Usuario registrado con éxito'}, 200



class UserGet(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        
        return user.json()
        
class SelectPj(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        user.select_character(num_pj=data['pj'])


"""
tener flask corriendo:
python app.py

consola python (open the data base):
import app
from app import db, create_app
app = create_app()
with app.app_context():
    db.create_all()       ///enter - enter

console sqlite3: entrar con (sqlite3 /tmp/foo.db)
.schema
"""        
