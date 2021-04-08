from flask_restful import Resource, reqparse, Api
# Importamos el contenido de Service
from service.service import Service
# Importamos Jsonify y Make_Response()
from flask import jsonify, make_response

class Items(Resource):
    
    # Due to the name of the parameter must be the same as the route: /items/<item_name>
    def get(self, item_name):
        """Get an item by its name

        Args:
            item_name (string): name of the item

        Returns:
            make_response Object: Returns a custom make_response() object with with all item whose satified the criteria of hve the same name of the parameter
        """
        
        response = make_response(jsonify(Service.filter_by_name(item_name)))
        response.headers['custom-response'] = 'Item filter by name was returned'
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        response.headers['warning'] = 'Custom Warning, just appears when it\' an warning'
        
        return response
        # return Service.filter_by_name(item_name), 200
    
    def parseRequest(self):
        """Let us validate values from the Request through "reqparse" and its object: RequestParser()

        Returns:
            dict: Returns a Dictionary with the item already validatedº
        """
        
        # Nos permite validad el objeto Request y sus valores
        parser = reqparse.RequestParser(bundle_errors=True)
        # Name of item
        parser.add_argument('name', type=str, required=True, location='json', help="Name of the Item is required")
        # Sell_in of Item
        parser.add_argument('sell_in', type=int, required=True, location='json', help="Sell_in of the Item is required")
        # Quality
        parser.add_argument('quality', type=int, required=True, location='json', help="Quality of the Item is required")
        
        # Dictionary with all args from parser
        return parser.parse_args()
    
    
    def post(self):
        """Let us add a new item/resource

        Returns:
            make_response Object: Returns a custom make_response() object with a message of the item has been added
        """
        
        args_content = self.parseRequest()
        
        # Llamo al método post_items y le pasó el args_content
        Service.post_item(args_content)
        
        response = make_response(jsonify('New Item has been added'))
        response.headers['custom-response'] = 'The item was added successfully!'
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 201
        response.headers['warning'] = 'Custom Warning, just appears when it\' an warning'
        
        return response
        
        # return 'New Item has been added', 201
    
    def delete(self):
        """Let us delete an item/resource

        Returns:
            string: Returns a string with a message of the item has been deleted
        """
        
        args_content = self.parseRequest()
        
        Service.delete_item(args_content)
        
        # DELETE Request don't receive a Message Response
        return '', 204