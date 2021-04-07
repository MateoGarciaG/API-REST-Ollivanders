from flask_restful import Resource, Api

class Wellcome(Resource):

    def get(self):
        """Get a message of Welcome Ollivanders

        Returns:
            dict: Returns a dictionary with the wellcome message
        """
        return {'Welcome!': 'Ollivanders'}