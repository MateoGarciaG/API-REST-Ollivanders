
# marshal_with for validate and filter fields
# abort for check function
from flask_restful import marshal_with, fields, abort


class Service():
    
    resource_fields = {
            'name': fields.String,
            'sell_in': fields.Integer,
            'quality': fields.Integer
    }
    
    

