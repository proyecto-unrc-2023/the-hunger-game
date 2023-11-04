from flask_restful import Resource
from app import db 
from user.user import User, UserSchema
from flask import jsonify
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
        
class User(Resource):
    def get(self):
        user = User()
        schema = UserSchema()
"""
tener flask corriendo:

consola python:
import app
from app import db
with app.app_context():
...         db.create_all()       ///enter - enter


console sqlite3: entrar con (sqlite3 /tmp/foo.db)
.schema
"""        
