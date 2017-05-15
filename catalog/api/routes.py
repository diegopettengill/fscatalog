from flask import Blueprint, jsonify
from catalog.models import Product, Category, User
from catalog import app

api = Blueprint('api', __name__)

""" Returs all the categories in database """


@api.route('/categories')
def get_categories():
    categories = Category.query.all()
    return jsonify(Category=[i.serialize for i in categories])


""" Returs all the products in database """


@api.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify(Product=[i.serialize for i in products])


""" Returns a product by id """


@api.route('/products/<int:product_id>')
def get_product_by_id(product_id):
    product = Product.query.filter_by(id=product_id).first()
    return jsonify(Product=product.serialize)
