from flask_restful import Resource, Api
from repository.models import Item


class Wellcome(Resource):

    def get(self):
        return {'Welcome!': 'Ollivanders'}