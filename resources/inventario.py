from flask_restful import Resource
# Importamos el contenido de Service
from service.service import Service

class Inventario(Resource):
    
    def get(self):
        return Service.get_items(), 200
    