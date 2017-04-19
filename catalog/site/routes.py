from flask import Blueprint, render_template, send_from_directory
from catalog.models import Product, Category
from catalog import app

site = Blueprint('site', __name__, template_folder='templates')


# common variables to the app
@app.context_processor
def inject():
    # fetch all the categories
    categories = Category.query.all()
    return dict(categories=categories)


@site.route('/uploads/<filename>')
def uploads(filename):
    return send_from_directory('catalog/uploads/', filename)


@site.route('/')
def home():
    # fetch the last 12 products from the database
    products = Product.query.limit(12)

    return render_template(
        'home.html',
        products=products
    )


@site.route('/category/<slug>')
def category(slug):
    return render_template(
        'category/index.html'
    )


@site.route('/product/<int:product_id>/<product_slug>')
def product_view(product_id, product_slug):
    # fetch the last 12 products from the database
    product = Product.query.filter_by(id=product_id).first()

    return render_template(
        'products/view.html',
        product=product
    )
