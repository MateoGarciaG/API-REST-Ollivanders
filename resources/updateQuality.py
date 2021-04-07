from flask_restful import Resource
# Importamos el contenido de Service
from service.service import Service

class UpdateQuality(Resource):
    
    def get(self):
        
        return Service.update_quality()