from flask_restful import Resource
# Importamos el contenido de Service
from service.service import Service

class Sellin(Resource):
    
    # Due to the name of the parameter must be the same as the route: /items/sellin/<item_sell_in>
    def get(self, item_sell_in):
        """Gets those items whose sell_in is the same as the value from the parameter

        Args:
            item_sell_in (int): sell_in of the item

        Returns:
            list: Retuns a list with all item whose have the same sell_in
        """
        return Service.filter_by_sell_in(item_sell_in), 200