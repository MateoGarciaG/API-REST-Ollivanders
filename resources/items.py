from flask_restful import Resource
# Importamos el contenido de Service
from service.service import Service
from repository.models.items import Items

class Items(Resource):
    
    def get(self, item_name):
        
        return Service.get_items(item_name), 200