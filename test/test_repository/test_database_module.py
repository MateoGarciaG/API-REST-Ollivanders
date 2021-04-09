# from repository.db import Database

import json
import pytest

from service.service import Service

from repository.models.items import Items


@pytest.mark.db_test
def test_add_item_db(session):
    
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    assert add_item.name == "Conjured Mana Cake"
    assert add_item.sell_in == 5
    assert add_item.quality == 8
    
@pytest.mark.db_test
def test_get_items_db(session):
    
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    # Funciona, pero al parecer no carga los datos que ya están en la base de datos, por lo cual no tiene ninguno, lo que implica que tengo que agregar un nuevo objeto/row
    items_db = [item for item in session.query(Items).all()]
    
    assert len(items_db) == 1
    
@pytest.mark.db_test
def test_delete_item_db(session):
    
    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    # Ahora lo eliminamos
    session.query(Items).filter(Items.name=="Conjured Mana Cake", Items.sell_in==5, Items.quality==8).delete()
    session.commit()
    
    # Verificamos si efectivamente lo ha eliminado si ningún row es igual al que eliminamos, CAMBIARLO y REFACTORIZARLO
    for item in session.query(Items).all():
        
        assert item.name != "Conjured Mana Cake"
        assert item.sell_in != 5
        assert item.quality != 8
    
# @pytest.mark.db_test
# def test_udpate_quality_items_db(session):
    
# @pytest.mark.db_test
# def test_get_by_name_db(session):
    
# @pytest.mark.db_test
# def test_get_by_sellin_db(session):
    
# @pytest.mark.db_test
# def test_get_by_quality_db(session):
    



# @pytest.mark.db_test
# def test_add_item_db(client, session):
    
#     # request_post = {"name": "Conjured Mana Cake", "sell_in": 4, "quality": 7}
    
#     # response = client.post('/tests', json=request_post)
#     response = client.post("/items?name=Test&sell_in=4&quality=7")
    
#     # Mock a Model
#     # mock_items_model = mocker.path('flask_sqlalchemy')
    
    
#     assert json.loads(response.data) == {"message": "New Item has been added"}
    
# @pytest.mark.db_test
# def test_get_items_db(client, session):
    
#     # request_post = {"name": "Conjured Mana Cake", "sell_in": 4, "quality": 7}
    
#     # response = client.post('/tests', json=request_post)
#     response = client.get("/inventory")
    
#     # Mock a Model
#     # mock_items_model = mocker.path('flask_sqlalchemy')
    
    
#     assert json.loads(response.data) == [
#     {
#         "name": "+5 Dexterity Vest",
#         "quality": 20,
#         "sell_in": 10
#     },
#     {
#         "name": "Aged Brie",
#         "quality": 0,
#         "sell_in": 2
#     },
#     {
#         "name": "Elixir of the Mongoose",
#         "quality": 7,
#         "sell_in": 5
#     },
#     {
#         "name": "Sulfuras Hand of Ragnaros",
#         "quality": 80,
#         "sell_in": 0
#     },
#     {
#         "name": "Sulfuras Hand of Ragnaros",
#         "quality": 80,
#         "sell_in": -1
#     },
#     {
#         "name": "Backstage passes to a TAFKAL80ETC concert",
#         "quality": 20,
#         "sell_in": 15
#     },
#     {
#         "name": "Backstage passes to a TAFKAL80ETC concert",
#         "quality": 49,
#         "sell_in": 10
#     },
#     {
#         "name": "Backstage passes to a TAFKAL80ETC concert",
#         "quality": 49,
#         "sell_in": 5
#     },
#     {
#         "name": "Conjured Mana Cake",
#         "quality": 6,
#         "sell_in": 3
#     }
#     ]