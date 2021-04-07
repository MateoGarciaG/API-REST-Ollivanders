from flask_restful import Resource, Api
# Importamos el contenido de Service
from service.service import Service

class Quality(Resource):
    
    # Due to the name of the parameter must be the same as the route: /items/quality/<item_quality>
    def get(self, item_quality):
        """Gets those items whose quality is the same as the value from the parameter

        Args:
            item_quality (int): quality of the item

        Returns:
            list: Retuns a list with all item whose have the same quality
        """
        return Service.filter_by_quality(item_quality), 200