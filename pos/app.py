from flask import Flask, jsonify
import os
import logging
from flask_restplus import Api, Resource, fields, reqparse
from models import db, Inventory
import utils

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(
    os.getenv('MYSQL_USERNAME', 'directdevops'),
    os.getenv('MYSQL_PASSWORD', 'directdevops'),
    os.getenv('MYSQL_SERVER', 'localhost'),
    os.getenv('MYSQL_DATABASE', 'test'))
app.logger.debug("Database URI is {}".format(DATABASE_URI))
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

api = Api(app, version='0.1.1', title='Inventory Service', description='Inventory Service for k8s')

ns = api.namespace('inventory', description="Inventory Namespace")


inventory_parser = utils.get_inventory_parser()
inventory_model = utils.get_inventory_model(api)

@ns.route("/initialize")
@api.doc()
class Initialize(Resource):
    """
    Initialize Resource
    """

    @api.response(200, 'Success')
    @api.response(500, 'Error with database initialization')
    def get(self):
        """
        This method initializes the database
        :return:
        """
        try:
            app.logger.info("initializing database")
            db.create_all()
            return 'Database Created', 200
        except Exception as e:
            app.logger.error("Following Error occurred {}".format(str(e)))
            return jsonify({"error": e}), 500


@ns.route("/pos")
@api.doc()
class Inventory(Resource):
    """
    This resource will deal with Inventories
    """

    @ns.doc('list course')
    @ns.marshal_list_with(inventory_model)
    def get(self):
        return Inventory.query.all()


@app.route('/')
def hello_world():
    return 'Pi Data Center Demo!'


if __name__ == '__main__':
    app.run(port=os.getenv('APP_PORT', 8080), debug=True, host="0.0.0.0")