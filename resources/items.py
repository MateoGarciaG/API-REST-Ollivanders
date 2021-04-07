from flask_restful import Resource, reqparse
# Importamos el contenido de Service
from service.service import Service
from repository.models.items import Items

class Items(Resource):
    
    def get(self, item_name):
        """Get an item by its name

        Args:
            item_name (string): name of the item

        Returns:
            list: Returns a list with all item whose satified the criteria of hve the same name of the parameter
        """
        
        return Service.get_items(item_name), 200
    
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
            string: Returns a string with a message of the item have been added
        """
        
        args_content = self.parseRequest()
        
        # Llamo al método post_items y le pasó el args_content
        Service.post_items(args_content)
        
        return 'New Item has been added', 201