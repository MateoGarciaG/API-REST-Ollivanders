
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
        if not items:
            abort(404, message="There is not items that satisfied this criteria")
        return items
    
    
    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_name(name):
        return Service.check_items(Database.filter_by_name(name))
    
    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_sell_in(sell_in):
        return Service.check_items(Database.filter_by_sell_in(sell_in))
    

    @staticmethod
    @marshal_with(resource_fields)
    def filter_by_quality(quality):
        return Service.check_items(Database.filter_by_quality(quality))
    
    @staticmethod
    @marshal_with(resource_fields)
    def get_items():
        
        return Database.get_items()
    
    @staticmethod
    def post_items(args_content):
        
        Database.post_item(args_content)
        
        return jsonify({"state": "The Item was added."})
    
    @staticmethod
    def delete_items(args_content):
        
        Database.delete_item(args_content)
        
        return jsonify({"state": "The Item was deleted."})
    
    @staticmethod
    def update_quality():
        
        return Database.update_quality()