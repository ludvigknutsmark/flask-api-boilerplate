from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(load_only=True)
    username = fields.Str()
    password = fields.Str(load_only=True)

user_schema = UserSchema()
users_schema = UserSchema(many=True)