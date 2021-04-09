import pytest
from controller.factory import create_app
from repository.models.db_model import db as _db
class TestConfig(object):
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
    
@pytest.yield_fixture(scope='session')
def app():
    
    app = create_app()
    # Configuro la APP Flask para los TESTS
    app.config.from_object(TestConfig)
    # Le asigno la conexión mysql
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:power2021@127.0.0.1/ollivanders'
    
    # Abrimos el contexto de la aplicación
    app_contx = app.app_context()
    app_contx.push()
    
    yield app
    
    # Elimino el contexto de la Aplicación
    app_contx.pop()
    # with app.app_context():
    
    #     return app
    
        
@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.yield_fixture(scope='session')
def db(app):
    
    # from repository.models.db_model import db
    
    # _db.app = app
    _db.init_app(app)
    # Create all models
    _db.create_all()
    # Return APP FLASK, but we can add more things
    yield _db
    
    # db.session.remove()
    # Eliminó todos los Models
    _db.drop_all()
    
@pytest.fixture(scope='function', autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()
    
    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)
    
    db.session = session_
    
    yield session_
    
    transaction.rollback()
    connection.close()
    session_.remove()