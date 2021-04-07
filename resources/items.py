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