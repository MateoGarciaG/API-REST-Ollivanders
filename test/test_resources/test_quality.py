import pytest
import json

@pytest.mark.db_test
def test_quality(client):
    rv = client.get("/items/quality/80")
    assert rv.status_code == 200
    assert json.loads(rv.data) == [{
        "name": "Sulfuras Hand of Ragnaros",
        "quality": 80,
        "sell_in": 0
    },
    {
        "name": "Sulfuras Hand of Ragnaros",
        "quality": 80,
        "sell_in": -1
    }]
    

# @pytest.mark.quality
@pytest.mark.db_test
def test_quality_fail(client):
    rv = client.get("/items/quality/150")
    assert rv.status_code == 404
    assert json.loads(rv.data) == {
    "message": "There is not items that satisfied this criteria"}
    
    