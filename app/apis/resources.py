from flask import jsonify
from flask_restful import Resource
from .tribute_stats import TributeSchema  # Importa el esquema

class MenuResource(Resource):
    def get(self):
        # Datos a serializar
        data = {
            'life': 5,
            'force': 2,
            'alliance': 2,
            'tributes': 2
        }

        # Crea una instancia del esquema
        tribute_schema = TributeSchema()

        # Serializa los datos usando el esquema
        result = tribute_schema.dump(data)

        # Devuelve los datos serializados como una respuesta JSON
        return jsonify(result)

    def get_new_district(self):
        district = dict(number_district=2)
        schema = DistrictSchema()
        result = jsonify(schema.dump(district))
        
        return result