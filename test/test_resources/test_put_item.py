
import pytest

import json
    
    
@pytest.mark.db_test
def test_put_item(client):
    """Test the PUT request of Items resource, test if since a request it can update the content of an item

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    
    # request_post = {"name": "Conjured Mana Cake", "sell_in": 4, "quality": 7}
    
    # response = client.post('/tests', json=request_post)
    response = client.put("/items/id/9/?name=Sulfuras Hand of Ragnaros&sell_in=3&quality=6")
    
    # Mock a Model
    # mock_items_model = mocker.path('flask_sqlalchemy')
    
    
    assert json.loads(response.data) == {"message": "Item content updated successfully"}
    assert response.status_code == 201