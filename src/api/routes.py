from flask import Blueprint
from .service import show_index, get_user

index = Blueprint('index', __name__)
index.route("/", methods=['GET'])(show_index)
#------------------------------------
# This could be split into several files, where user get an own routes file. 
# This is just to show an example of multiple blueprints.
#------------------------------------
user = Blueprint('user', __name__)
user.route("/<id>", methods=['GET'])(get_user)