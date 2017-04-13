from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/getCatalog')
def getCatalog():
    return '{"result": "API OBJ"}'

#
# @app.route("/api/itens/<int:restaurant_id>/")
# def api_menu_itens(restaurant_id):
#     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
#     items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
#     return jsonify(MenuItem=[i.serialize for i in items])