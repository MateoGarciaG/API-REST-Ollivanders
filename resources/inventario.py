from flask_restful import Resource, Api
# Importamos el contenido de Service
from service.service import Service
# Importamos el make_response
from flask import make_response, jsonify


class Inventario(Resource):
    
    def get(self):
        """Gets a list of all items.
        Makes a custom Response Object

        Returns:
            list: Returns a List with items, each item is a dictionary
        """
        # response = Response(response=json.dump(Service.get_items()), mimetype='application/json', status=200, )
        
        response = make_response(jsonify(Service.get_items()))
        response.headers['custom-response'] = 'All Items returned'
        response.headers['Content-Type'] = 'application/json'
        response.status_code = 200
        response.headers['warning'] = 'Custom Warning, just appears when it\' an warning'
        # MimeType es más específico
        # response.mimetype = "application/json"
        
        
        
        return response
        # return Service.get_items(), 200
    