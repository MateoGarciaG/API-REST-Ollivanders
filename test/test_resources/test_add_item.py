
import pytest

import json
    
    
@pytest.mark.db_test
# def test_post_item(client, session):
def test_post_item(client):
    
    # request_post = {"name": "Conjured Mana Cake", "sell_in": 4, "quality": 7}
    
    # response = client.post('/tests', json=request_post)
    response = client.post("/items?name=Conjured%20Mana%20Cake&sell_in=4&quality=7")
    
    # Mock a Model
    # mock_items_model = mocker.path('flask_sqlalchemy')
    
    
    assert json.loads(response.data) == {"message": "New Item has been added"}
    assert response.status_code == 201