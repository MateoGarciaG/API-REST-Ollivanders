from flask import Flask
from flask_restful import Resource, Api

#* App FLASK
app = Flask(__name__)
api = Api(app)

class HelloOllivanders(Resource):
    def get(self):
        return {'hello': 'Ollivander'}

api.add_resource(HelloOllivanders, '/')

if __name__ == '__main__':
    app.run(debug=True)
    