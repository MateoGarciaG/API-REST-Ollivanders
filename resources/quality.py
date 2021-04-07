from flask_restful import Resource
# Importamos el contenido de Service
from service.service import Service

class Quality(Resource):
    
    # Due to the name of the parameter must be the same as the route: /items/quality/<item_quality>
    def get(self, item_quality):
        
        return Service.filter_by_quality(item_quality), 200