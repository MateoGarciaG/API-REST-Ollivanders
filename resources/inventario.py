from flask_restful import Resource, Api
# Importamos el contenido de Service
from service.service import Service

class Inventario(Resource):
    
    def get(self):
        """Gets a list of all items

        Returns:
            list: Returns a List with items, each item is a dictionary
        """
        return Service.get_items(), 200
    