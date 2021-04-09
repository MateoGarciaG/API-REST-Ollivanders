
import pytest

import json
    
    
@pytest.mark.db_test
def test_delete_item(client):
    
    # request_post = {"name": "Conjured Mana Cake", "sell_in": 4, "quality": 7}
    
    # response = client.post('/tests', json=request_post)
    # response = client.post("/items?name=Conjured%20Mana%20Cake&sell_in=3&quality=6")
    response_delete = client.delete("/items?name=Conjured%20Mana%20Cake&sell_in=3&quality=6")
    
    # Mock a Model
    # mock_items_model = mocker.path('flask_sqlalchemy')
    
    # Debido a que el HTTP DELETE no retorna ninguna respuesta por defecto, lo mejor es simplemente verificar si el contenido de la Response si está vacía mediante b"" // b = significa byte. Para Transformar el string en Bytes
    assert b"" in response_delete.data
    assert response_delete.status_code == 204