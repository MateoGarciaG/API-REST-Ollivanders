from flask import g
from flask_restful import abort
# Importamos el método get_db() para poder manipular la Base de Datos
from repository.db_connection import get_db

class Database():
    
    """Database Class: This class contains all methods that let us filter, search, update, deleting our database, basically consist of a serie of methods that let us manipulate the dabase. For this reason, this class contains the logic of this manipulation of database, which it's important because this class belong to Repository Module where this module is where all related to database is. The main advantage fo this class is that other module can use this class and use these methods without knowling the logic behind, so for example. Service module doesn't need to implement logic to manipulate Database in its module, but Service module can directly use this class to manipulate Database. There is less coupling.
    """
    
    @staticmethod
    def filter_by_name(name):
        
        db = get_db()
        
        itemsList = []
        
        # Necesito crear un bucle debido a que el resultado de la QUERY es un objeto con todos los resultados.
        for item in g.Items.query.filter_by(name=name):
            itemsList.append(item)
            
        return itemsList
        
    @staticmethod
    def filter_by_sell_in(sell_in):
        
        db = get_db()
        
        itemsList = []
        
        for item in g.Items.query.filter_by(sell_in=sell_in):
            itemsList.append(item)
            
        return itemsList
    
    @staticmethod
    def filter_by_quality(quality):
        
        db = get_db()
        
        itemsList = []
        
        for item in g.Items.query.filter_by(quality=quality):
            itemsList.append(item)
            
        return itemsList
    
    @staticmethod
    def get_items():
        
        db = get_db()
        
        itemsList = []
        
        for item in g.Items.query.all():
            itemsList.append(item)
            
        return itemsList
    
    @staticmethod
    def post_item(args_content):
        
        db = get_db()
        
        add_item = g.Items(name=args_content["name"], sell_in=args_content["sell_in"], quality=args_content["quality"])
        
        db.session.add(add_item)
        db.session.commit()
        
    @staticmethod
    def delete_item():
        
        
        
    @staticmethod
    def update_quality():
        
    @staticmethod
    def check_items(items):
        if not items:
            abort(404, message="There is not items that match this criteria")
        return list(items)