import pytest

@pytest.mark.hello_world
def test_hello_world(client):
    rv = client.get('/')
    assert b'{"hello": "Ollivander"}' in rv.data
