#!/usr/bin/env python3
from flask import Flask

# models
from .models import User

# database
from .database import db

# blueprints
from .routes import index, user

def create_app():
    template_dir=""
    app = Flask(__name__, static_folder='static', static_url_path='',template_folder=template_dir)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Register blueprints
    app.register_blueprint(index, url_prefix="/")
    app.register_blueprint(user, url_prefix="/api/user")
    
    # Database initialization with some data
    db.init_app(app)
    with app.app_context():
        db.create_all()
    
        # Add test users
        users = [
            User(username="admin", password="admin"),
            User(username="user", password="user")
        ]

        for item in users:
            db.session.add(item)
        db.session.commit()
    
    return app