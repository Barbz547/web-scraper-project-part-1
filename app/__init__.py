from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager, login_manager

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'codingtemple'
    app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://havhttks:hpDlb3m8Blo3MLCnB7nkFUyAae9N8d-W@batyr.db.elephantsql.com/havhttks') or f'sqlite:///{DB_NAME}'
    db.init_app(app)
    migrate.init_app(app, db)

    
    from.views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database=app

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # where we want to go if not logged in
    login_manager.init_app(app)


    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

    def create_database(app):
        if not path.exists('app/' + DB_NAME):
            db.create_all(app=app)
            print('Created Database!')

