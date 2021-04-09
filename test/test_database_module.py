# from repository.db import Database

import json
import pytest

@pytest.mark.db_test
def test_save_request(client):
    
    # request_post = {"name": "Conjured Mana Cake", "sell_in": 4, "quality": 7}
    
    # response = client.post('/tests', json=request_post)
    response = client.post("/items?name=Test&sell_in=4&quality=7")
    
    assert json.loads(response.data) == {"message": "New Item has been added"}