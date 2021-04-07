from flask_restful import Resource
# Importamos el contenido de Service
from service.service import Service

class Sellin(Resource):
    
    # Due to the name of the parameter must be the same as the route: /items/sellin/<itemSellin>
    def get(self, itemSellIn):
        return Service.filter_by_sell_in(itemSellIn), 200