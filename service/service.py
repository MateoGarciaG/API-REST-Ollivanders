
# marshal_with for validate and filter fields
# abort for check function
from flask_restful import marshal_with, fields, abort
from flask import jsonify

# Importamos la Database Class con los métodos
from repository.db import *
class Service():
    
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
    def filter_by_name(name):
        return Service.check_items(Database.filter_by_name(name))
    
    @staticmethod
    def filter_by_sell_in(sell_in):
        return Service.check_items(Database.filter_by_sell_in(sell_in))
    

    @staticmethod
    def filter_by_quality(quality):
        return Service.check_items(Database.filter_by_quality(quality))
    
    @staticmethod
    @marshal_with(resource_fields)
    def get_items():
        
        return Database.get_items()