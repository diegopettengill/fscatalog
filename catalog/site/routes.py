from flask import Blueprint, render_template, send_from_directory
from catalog.models import Product

site = Blueprint('site', __name__, template_folder='templates')


@site.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory('catalog/uploads/', filename)


@site.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)
