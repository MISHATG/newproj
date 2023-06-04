from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def main_app():
    
    app = Flask(__name__)
    app.config["SECRET_KEY"]="this is a secret key"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    db.init_app(app)
    from .models import User
    
    with app.app_context():
        db.create_all()
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    
    return app   

def create_db(app):
    if not path.exists("mysite/" + DB_NAME):
        db.create_all(app=app)
        print('database created')  