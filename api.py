from flask import Flask
from flask_restful import Resource, Api

# Repository Module
from repository.db_connection import init_app

#* App FLASK
app = Flask(__name__)

# Init APP
init_app(app)

# API RESTful
api = Api(app)

class HelloOllivanders(Resource):
    def get(self):
        return {'hello': 'Ollivander'}

api.add_resource(HelloOllivanders, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    