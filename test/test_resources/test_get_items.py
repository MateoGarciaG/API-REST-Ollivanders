
import pytest
import json

defaultInventory = [
    {
        "name": "+5 Dexterity Vest",
        "quality": 20,
        "sell_in": 10
    },
    {
        "name": "Aged Brie",
        "quality": 0,
        "sell_in": 2
    },
    {
        "name": "Elixir of the Mongoose",
        "quality": 7,
        "sell_in": 5
    },
    {
        "name": "Sulfuras Hand of Ragnaros",
        "quality": 80,
        "sell_in": 0
    },
    {
        "name": "Sulfuras Hand of Ragnaros",
        "quality": 80,
        "sell_in": -1
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 20,
        "sell_in": 15
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 49,
        "sell_in": 10
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 49,
        "sell_in": 5
    },
    {
        "name": "Conjured Mana Cake",
        "quality": 6,
        "sell_in": 3
    }
    ]

@pytest.mark.db_test
def test_get_items(client):
    """Test the GET request of Inventario resource, test if since a request it can get all items

    Args:
        client (test_client Flask): It's the test_client() object from APP Flask
    """
    
    # request_post = {"name": "Conjured Mana Cake", "sell_in": 4, "quality": 7}
    
    # response = client.post('/tests', json=request_post)
    response = client.get("/inventory")
    
    # Mock a Model
    # mock_items_model = mocker.path('flask_sqlalchemy')
    
    
    assert json.loads(response.data) == defaultInventory
    assert response.status_code == 200