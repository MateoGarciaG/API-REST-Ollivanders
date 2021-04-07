from flask_restful import Resource
# Importamos el contenido de Service
from service.service import Service

class UpdateQuality(Resource):
    
    def get(self):
        """Gets a list of all items with their quality updated

        Returns:
            list: Returns a List with items, each item is a dictionary
        """
        return Service.update_quality()