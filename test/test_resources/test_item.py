
import pytest

import json
    
    
# Item inside db
# @pytest.mark.item
@pytest.mark.db_test
def test_item(client):
    rv = client.get("/items/name/Aged Brie")
    assert json.loads(rv.data) == [{"name": "Aged Brie", "sell_in": 2, "quality":0}]
    assert rv.status_code == 200


# Request without Item Name
# @pytest.mark.item
# @pytest.mark.non_name
@pytest.mark.db_test
def test_item_name_fail(client):
    rv = client.get("/items/name/<name>")
    assert rv.status_code == 404
    assert json.loads(rv.data) == {"message": "There is not items that satisfied this criteria"}
    