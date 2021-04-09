import pytest
import json

@pytest.mark.db_test
def test_sell_in(client):
    rv = client.get("/items/sellin/10")
    assert rv.status_code == 200
    assert json.loads(rv.data) == [{
        "name": "+5 Dexterity Vest",
        "quality": 20,
        "sell_in": 10
    },{
        "name": "Backstage passes to a TAFKAL80ETC concert",
        "quality": 49,
        "sell_in": 10
    }]
    
# @pytest.mark.sell_in
@pytest.mark.db_test
def test_sell_in_fail(client):
    rv = client.get("/items/sellin/150")
    assert rv.status_code == 404
    assert json.loads(rv.data) == {
    "message": "There is not items that satisfied this criteria"}
    
    