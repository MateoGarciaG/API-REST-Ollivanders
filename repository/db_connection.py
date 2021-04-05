from flask_sqlalchemy import SQLAlchemy
from flask import g
# Import current_app for using inside of SQLAlchemy Object
from flask import current_app as app

# Click Package
import click
from flask.cli import with_appcontext

# Models
# from repository.models import Inventory



def get_db():
    
    if "db" not in g:
        
        # SQLite
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseCarpeta/nombreDB.db'
        # MYSQL
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:power2021@127.0.0.1/ollivanders'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        # Agrego el current_app con la APP de flask dentro del objeto SQLAlchemy
        g.db = SQLAlchemy(app)
        
        # Aún no he creado el Inventory Model
        # g.Inventory = Inventory
        
        return g.db


def close_db(e=None):
    # Si la conexión existe, se cierra.
    # Este método lo he visto también en la documentación oficial
    # https://flask.palletsprojects.com/en/1.1.x/appcontext/
    db = g.pop('db', None)

    if db is not None:
        db.close()
