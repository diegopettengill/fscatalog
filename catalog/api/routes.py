from flask import Blueprint, jsonify
from catalog.models import Product, Category, User
from catalog import app

api = Blueprint('api', __name__)


@api.route('/categories')
def get_categories():
    categories = Category.query.all()
    return jsonify(Category=[i.serialize for i in categories])


@api.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify(Product=[i.serialize for i in products])
    #
    # @app.route("/api/itens/<int:restaurant_id>/")
    # def api_menu_itens(restaurant_id):
    #     restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    #     items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    #     return jsonify(MenuItem=[i.serialize for i in items])
