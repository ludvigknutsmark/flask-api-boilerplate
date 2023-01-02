from .models import User
from .schemas import user_schema

def show_index():
    return "<p>Hello, Flask Boilerplate!</p>"

def get_user(id):
    user = User.query.filter_by(id=id).first()
    return user_schema.dump(user)