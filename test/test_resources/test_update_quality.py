
import pytest
import json


expected_updated_inventory = [
    {
        "name": "+5 Dexterity Vest",
        "quality": 18,
        "sell_in": 9
    },
    {
        "name": "Aged Brie",
        "quality": 1,
        "sell_in": 1
    },
    {
        "name": "Elixir of the Mongoose",
        "quality": 6,
        "sell_in": 4
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
        "quality": 21,
        "sell_in": 14
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 50,
        "sell_in": 9
    },
    {
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 50,
        "sell_in": 4
    },
    {
        "name": "Conjured Mana Cake",
        "quality": 4,
        "sell_in": 2
    }]

@pytest.mark.db_test
def test_update_quality(client):
    
    response = client.get("/update_quality")
    
    assert json.loads(response.data) == expected_updated_inventory