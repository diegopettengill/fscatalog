from flask import Blueprint, render_template, send_from_directory
from catalog.models import Product, Category

site = Blueprint('site', __name__, template_folder='templates')


@site.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory('catalog/uploads/', filename)


@site.route('/')
def home():

    # fetch the last 12 products from the database
    products = Product.query.limit(12)

    # fetch all the categories
    categories = Category.query.all()

    return render_template('home.html', products=products, categories=categories)
