from flask import Flask
from flask_restful import Resource, Api

# Import Resources
from resources.wellcome import Wellcome
from resources.inventario import Inventario
from resources.updateQuality import UpdateQuality
from resources.items import Items
from resources.quality import Quality
from resources.sellin import SellIn

# Import from Repository the db_connection.py
from repository import db_connection

def create_app():

    app = Flask(__name__)
    
    # Init the Flask APP
    db_connection.init_app()

    #API REST to be able to test
    api = Api(app, catch_all_404s=True)

    # Add Resources
    api.add_resource(Wellcome, '/')
    api.add_resource(Inventory, '/inventory')
    api.add_resource(Items, '/items/name/<string:item_name>', '/items')
    api.add_resource(Sellin, '/items/sellin/<int:item_sell_in>')
    api.add_resource(Quality, '/items/quality/<int:item_quality>')
    api.add_resource(UpdateQuality, '/update_quality')

    return app

if __name__=='__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)