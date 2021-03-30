import pytest
from controller.hello_ollivanders import create_app

@pytest.fixture
def client():
    app = create_app()    
    return app.test_client()