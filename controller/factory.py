from flask import Flask
from flask_restful import Resource, Api

# Import Resources
from resources.inventario import Inventario
from resources.updateQuality import UpdateQuality
from resources.items import Items
from resources.quality import Quality
from resources.sellin import SellIn

def create_app():

    app = Flask(__name__)

    #API REST to be able to test
    api = Api(app, catch_all_404s=True)

    class HelloOllivanders(Resource):
        def get(self):
            return {"hello": "Ollivander"}

    api.add_resource(HelloOllivanders, '/')

    return app

if __name__=='__main__':
    app = create_app()
    app.run(debug=True)