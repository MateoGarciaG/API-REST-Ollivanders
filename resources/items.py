from flask_restful import Resource
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