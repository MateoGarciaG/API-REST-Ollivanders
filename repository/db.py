from flask import g
# Importamos el método get_db() para poder manipular la Base de Datos
from repository.db_connection import get_db

# Importamos el método createObjectItem() de repo.py para poder crear un objeto a partir de la info del item
from repository.repo import Factory

class Database():
    
    """Database Class: This class contains all methods that let us filter, search, update, deleting our database, basically consist of a serie of methods that let us manipulate the dabase. For this reason, this class contains the logic of this manipulation of database, which it's important because this class belong to Repository Module where this module is where all related to database is. The main advantage fo this class is that other module can use this class and use these methods without knowling the logic behind, so for example. Service module doesn't need to implement logic to manipulate Database in its module, but Service module can directly use this class to manipulate Database. There will be less coupling.
    """
    
    @staticmethod
    def filter_by_name(name):
        """Let us filter an Item by the name of this item

        Args:
            name (string): Name of the Item

        Returns:
            list: Returns a List of Items that satisfies the query of Items Query Model
        """
        
        db = get_db()
        
        # itemsList = []
        
        # Necesito crear un bucle debido a que el resultado de la QUERY es un objeto con todos los resultados.
        # for item in g.Items.query.filter_by(name=name):
        #     itemsList.append(item)
            
        itemsList = [item for item in g.Items.query.filter_by(name=name)]
            
        return itemsList
        
    @staticmethod
    def filter_by_sell_in(sell_in):
        """Let us filter an Item by the sell_in of this item

        Args:
            sell_in (int): Sell_in of the Item

        Returns:
            list: Returns a List of Items that satisfies the query of Items Query Model, in this case. Those items whose have that sell_in
        """
        
        db = get_db()
        
        # itemsList = []
        
        # for item in g.Items.query.filter_by(sell_in=sell_in):
        #     itemsList.append(item)
            
        itemsList = [item for item in g.Items.query.filter_by(sell_in=sell_in)]
            
        return itemsList
    
    @staticmethod
    def filter_by_quality(quality):
        """Let us filter an Item by the quality of this item

        Args:
            quality (int): quality of the Item

        Returns:
            list: Returns a List of Items that satisfies the query of Items Query Model, in this case. Those items whose have that quality
        """
        
        db = get_db()
        
        # itemsList = []
        
        # for item in g.Items.query.filter_by(quality=quality):
        #     itemsList.append(item)
            
        itemsList = [item for item in g.Items.query.filter_by(quality=quality)]
            
        return itemsList
    
    @staticmethod
    def get_items():
        
        """Get All Items from Database

        Returns:
            (list): Returns a list with all Items
        """
        
        db = get_db()
        
        # itemsList = []
        
        # for item in g.Items.query.all():
        #     itemsList.append(item)
            
        itemsList = [item for item in g.Items.query.all()]
            
        return itemsList
    
    @staticmethod
    def post_item(args_content):
        """Add a new item into de Database Ollivanders into the Items Table, don't return nothing

        Args:
            args_content (dict): Contains the dictionary from parse_args() method, which in the other module let us validate the Request object values
        """
        db = get_db()
        
        add_item = g.Items(name=args_content["name"], sell_in=args_content["sell_in"], quality=args_content["quality"])
        
        db.session.add(add_item)
        db.session.commit()
        
    @staticmethod
    def delete_item(args_content):
        """Delete an item into de Database Ollivanders into the Items Table, don't return nothing

        Args:
            args_content (dict): Contains the dictionary from parse_args() method, which in the other module let us validate the Request object values
        """
        
        db = get_db()
        
        delete_item = g.Items.query.filter_by(name=args_content['name'], sell_in=args_content['sell_in'],quality=args_content['quality']).first()
        
        db.session.delete(delete_item)
        db.session.commit()
        
        
    @staticmethod
    def update_quality():
        """Update the quality of ALL items that we have in DataBase and after we return the entire Inventory to the Cliente

        Returns:
            (list): Returns a list with all Items, each item is a dictionary
        """
        
        db = get_db()
        
        for item in g.Items.query.all():
            
            # Creamos el objeto Item a partir de la info de la Lista que insertamos en los párametros del método: createObjectItem()
            itemObject = Factory.createObjectItem([item.name, item.sell_in, item.quality])
            
            # Actualizamos la calidad del item
            itemObject.update_quality()
            
            # Actualizamos los datos de cada item
            item.sell_in = itemObject.get_sell_in()
            item.quality = itemObject.get_quality()
            # Guardamos los datos actualizados
            db.session.commit()
        
        return Database.get_items()
    