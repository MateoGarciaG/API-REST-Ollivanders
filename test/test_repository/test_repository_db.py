# from repository.db import Database

import json
import pytest

from service.service import Service

from repository.models.items import Items

# Importamos Factory con el createObjectITem()
from repository.repo import Factory


@pytest.mark.db_test
def test_add_item_db(session):
    """Test if through session we can add an item

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """
    
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    assert add_item.name == "Conjured Mana Cake"
    assert add_item.sell_in == 5
    assert add_item.quality == 8
    
@pytest.mark.db_test
def test_get_items_db(session):
    """Test if through session we can get all items

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """
    
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    # Funciona, pero al parecer no carga los datos que ya están en la base de datos, por lo cual no tiene ninguno, lo que implica que tengo que agregar un nuevo objeto/row
    items_db = [item for item in session.query(Items).all()]
    
    assert len(items_db) == 1
    
@pytest.mark.db_test
def test_delete_item_db(session):
    """Test if through session we can delete an item

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """
    
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
    
@pytest.mark.db_test
def test_udpate_quality_items_db(session):
    """Test if through session we can update the quality of all items

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """
    
    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    for item in session.query(Items).all():
        
        # Creamos el objeto Item a partir de la info de la Lista que insertamos en los párametros del método: createObjectItem()
        itemObject = Factory.createObjectItem([item.name, item.sell_in, item.quality])
        
        # Actualizamos la calidad del item
        itemObject.update_quality()
        
        # Actualizamos los datos de cada item
        item.sell_in = itemObject.get_sell_in()
        item.quality = itemObject.get_quality()
        # Guardamos los datos actualizados
        session.commit()
        
        # Testeamos si efectivamente se actualizo el item
        assert item.name == "Conjured Mana Cake"
        assert item.sell_in == 4
        assert item.quality == 6
    
    
@pytest.mark.db_test
def test_get_by_name_db(session):
    """Test if through session we can get an item by its name

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """
    
    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    # Get el item por su nombre, en este caso como solo hay un item de esa calidad, retornará el del conjured mana cake
    get_conjured_by_name = session.query(Items).filter(Items.name=="Conjured Mana Cake").first()
    
    assert get_conjured_by_name.name == "Conjured Mana Cake"
    assert get_conjured_by_name.sell_in == 5
    assert get_conjured_by_name.quality == 8
    
    
    
    
    
@pytest.mark.db_test
def test_get_by_sellin_db(session):
    """Test if through session we can get an item by its sell_in

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """
    
    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    # Get el item por su sell_in, en este caso como solo hay un item de esa calidad, retornará el del conjured mana cake
    get_conjured_by_sellin = session.query(Items).filter(Items.sell_in==5).first()
    
    assert get_conjured_by_sellin.name == "Conjured Mana Cake"
    assert get_conjured_by_sellin.sell_in == 5
    assert get_conjured_by_sellin.quality == 8
    
@pytest.mark.db_test
def test_get_by_quality_db(session):
    """Test if through session we can get an item by its quality

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """
    
    # Añadimos el item
    add_item = Items("Conjured Mana Cake", 5, 8)
    
    session.add(add_item)
    session.commit()
    
    # Get el item por su calidad, en este caso como solo hay un item de esa calidad, retornará el del conjured mana cake
    get_conjured_by_quality = session.query(Items).filter(Items.quality==8).first()
    
    assert get_conjured_by_quality.name == "Conjured Mana Cake"
    assert get_conjured_by_quality.sell_in == 5
    assert get_conjured_by_quality.quality == 8
    