from flask_restplus import reqparse, fields, Api


def get_inventory_parser():
    """
    This method returns the inventory parse
    :return:
    """
    inventory_parser = reqparse.RequestParser()
    inventory_parser.add_argument('id', type=int)
    inventory_parser.add_argument('name')
    inventory_parser.add_argument('description')
    inventory_parser.add_argument('itemscount', type=int)
    return inventory_parser


def get_inventory_model(api):
    """

    :type api: Api
    """
    inventory_model = api.model('InventoryModel', {
        'id': fields.Integer,
        'name': fields.String,
        'description': fields.String,
        'itemscount': fields.Integer
    })
    return inventory_model
