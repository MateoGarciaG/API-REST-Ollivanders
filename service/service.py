
# marshal_with for validate and filter fields
# abort for check function
from flask_restful import marshal_with, fields, abort
from flask import jsonify

# Importamos la Database Class con los métodos
from repository.db import *
class Service():
    """Service: This class consist of a serie of methods that interact with Database/repository Module, where through these methods we can get or manipulate the data of database to send to the client with the Response

    """
    
    # Estructura de campos que serán usados en el marshal_with()
    resource_fields = {
            'name': fields.String,
            'sell_in': fields.Integer,
            'quality': fields.Integer
    }
    
    @staticmethod
    def check_items(items):
        """Check if the items are not empty or not, if it's empty throw an Abort()

        Args:
            items (list): List of items

        Returns:
            (list): If the list is not empty, returns the same list
        """
        if not items:
            abort(404, message="There is not items that satisfied this criteria")
        return items
    
    
    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_name(name):
        """Return those items who satisfied the criteria of db.py method: Database.filter_by_name(). It's basically filter those items whose name is the same as the parameter

        Args:
            name (string): The name of the item

        Returns:
            list: Returns a list from the result of the method: Database.filter_by_name()
        """
        return Service.check_items(Database.filter_by_name(name))
    
    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_sell_in(sell_in):
        """Return those items who satisfied the criteria of db.py method: Database.filter_by_sell_in(). It's basically filter those items whose sell_in is the same as the parameter

        Args:
            sell_in (int): The sell_in of the item

        Returns:
            list: Returns a list from the result of the method: Database.filter_by_sell_in()
        """
        return Service.check_items(Database.filter_by_sell_in(sell_in))
    

    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_quality(quality):
        """Return those items who satisfied the criteria of db.py method: Database.filter_by_quality(). It's basically filter those items whose quality is the same as the parameter

        Args:
            quality (int): The quality of the item

        Returns:
            list: Returns a list from the result of the method: Database.filter_by_quality()
        """
        return Service.check_items(Database.filter_by_quality(quality))
    
    @staticmethod
    @marshal_with(resource_fields)
    def get_items():
        """Return all items from our Database through the method: Database.get_items()

        Returns:
            list: Returns a list from the result of the method: Database.get_items()
        """
        
        return Database.get_items()
    
    @staticmethod
    def post_items(args_content):
        """Add a new item, this through the method: Database.post_item() whose receive the args_content parameter

        Args:
            args_content (dict): A dictionary that contains data from an Item

        Returns:
            dict: Returns a Dictionary with format of a Jsonify
        """
        
        Database.post_item(args_content)
        
        return jsonify({"state": "The Item was added."})
    
    @staticmethod
    def delete_items(args_content):
        """Delete an item, this through the method: Database.delete_item() whose receive the args_content parameter

        Args:
            args_content (dict): A dictionary that contains data from an Item

        Returns:
            dict: Returns a Dictionary with format of a Jsonify
        """
        
        Database.delete_item(args_content)
        
        return jsonify({"state": "The Item was deleted."})
    
    @staticmethod
    def update_quality():
        
        return Database.update_quality()