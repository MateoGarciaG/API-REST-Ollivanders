import pytest
# APP Flask Factory
from controller.factory import create_app
# Repo.py Factory para poblar la base de datos test
from repository.models.db_model import db as _db
from repository.repo import Factory
# Importamos también el modelo
from repository.models.items import Items
# Para la conexión de la DB test, importó el objeto G de Flask
# from flask import g
from repository.db_connection import init_app

class TestConfig(object):
    # DEBUG debe ser Falso para que no haya error del método SETUP al intentar ejecutar el APP Flask, por ahora es mejor dejarlo en False
    DEBUG = False
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'test'
    TESTING = True

# @pytest.fixture
# def client():
#     app = create_app()    
#     return app.test_client()

# @pytest.fixture
# def client():
#     app = create_app()  
    
#     app.config.from_object("config.TestingConfig") 
    
#     with app.app_context():
#         with app.test_client() as client:
#             yield client
    
#     return app.test_client()
    
# scope='session' tiene un alcance durante todo el proceso de la request
# @pytest.yield_fixture(scope='session')
# @pytest.fixture(scope='session')
# def app():
    
#     app = create_app()
#     # Configuro la APP Flask para los TESTS
#     app.config.from_object(TestConfig)
#     # Le asigno la conexión mysql
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:power2021@127.0.0.1/ollivanderstest'
    
#     # Abrimos el contexto de la aplicación
#     app_contx = app.app_context()
#     app_contx.push()
    
    
#     yield app
    
#     # Elimino el contexto de la Aplicación
#     app_contx.pop()
#     # with app.app_context():
    
#     #     return app
    
        
# @pytest.fixture(scope='session')
# def client(app):
    
#     return app.test_client()


# # @pytest.yield_fixture(scope='session')
# @pytest.fixture(scope='session')
# def db(app):
    
#     # from repository.models.db_model import db
    
#     # _db.app = app
#     _db.init_app(app)
#     # Create all models
#     _db.create_all()
    
#     # Obtenemos la lista con los items
#     # inventario = Factory.loadInventory()
    
#     # # Poblamos la Base de datos introduciendo los datos
#     # for item in inventario:
        
#     #     add_item = Items(name=item["name"], sell_in=item["sell_in"], quality=item["quality"])
        
#     #     _db.session.add(add_item)
#     #     _db.session.commit()
    
    
    
#     # Return APP FLASK, but we can add more things
#     yield _db
    
#     _db.session.remove()
#     # Eliminó todos los Models
#     # _db.drop_all()
    
# # Tiene el scope='function' para que su alcance solo sea cada test
# @pytest.fixture(scope='function', autouse=True)
# def session(db):
#     connection = db.engine.connect()
#     transaction = connection.begin()
    
#     options = dict(bind=connection, binds={})
#     session_ = db.create_scoped_session(options=options)
    
#     db.session = session_
    
#     yield session_
    
#     transaction.rollback()
#     connection.close()
#     session_.remove()
    
    
# class DBConnectionTest():
    
#     def get_db_test():
    
#         # Si la propiedad "db" no está en el objeto G, entonces:
#         if "db" not in g:
            
#             # SQLite
#             # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databaseCarpeta/nombreDB.db'
#             # MYSQL
#             app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:power2021@127.0.0.1/ollivanders'
#             app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            
#             # Agrego el current_app con la APP de flask dentro del objeto SQLAlchemy
#             db.init_app(app)
#             g.db = db
            
#             # Agregamos al objeto G, la propiedad ITEMS con el valor del modelo Items
#             g.Items = Items
            
#             return g.db
    
    
    
@pytest.fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            _db.init_app(app)
            # _db.drop_all()
            _db.create_all()
            
            #         Obtenemos la lista con los items
            inventario = Factory.loadInventory()
            
            # Poblamos la Base de datos introduciendo los datos
            for item in inventario:
                
                add_item = Items(name=item["name"], sell_in=item["sell_in"], quality=item["quality"])
                
                _db.session.add(add_item)
                _db.session.commit()
            
            yield client
            
            _db.session.query(Items).delete()
            _db.session.commit()
            # _db.session.close()
            # _db.drop_all()
            
            
@pytest.fixture(scope='function')
def db(app):
    with app.test_client() as client:
        with app.app_context():
            _db.init_app(app)
            # _db.drop_all()
            _db.create_all()
            
            #         Obtenemos la lista con los items
            inventario = Factory.loadInventory()
            
            # Poblamos la Base de datos introduciendo los datos
            for item in inventario:
                
                add_item = Items(name=item["name"], sell_in=item["sell_in"], quality=item["quality"])
                
                _db.session.add(add_item)
                _db.session.commit()
            
            yield _db
            
            _db.session.query(Items).delete()
            _db.session.commit()


# Tiene el scope='function' para que su alcance solo sea cada test
@pytest.fixture(scope='function', autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()
    
    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)
    
    db.session = session_
    
    yield session_
    
    transaction.rollback()
    # connection.close()
    session_.remove()

# @pytest.fixture
# def db(app):
#     app.app_context().push()
#     _db.init_app(app)
#     _db.create_all()
#     yield _db
#     _db.session.close()
#     _db.drop_all()
