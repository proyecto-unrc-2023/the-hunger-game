from marshmallow import Schema, fields

class TributeSchema(Schema):
    life = fields.Integer()
    force = fields.Integer()
    alliance = fields.Integer()
    tributes = fields.Integer()