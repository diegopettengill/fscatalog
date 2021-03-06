import os
from flask import Blueprint, render_template, send_from_directory, request, \
    url_for, redirect, session, json, flash
from catalog.models import Product, Category, User
from catalog import app
from flask import make_response
from flask.ext.login import LoginManager, login_required, login_user, \
    logout_user, current_user, UserMixin
from requests_oauthlib import OAuth2Session
from requests.exceptions import HTTPError
from database import db_session, exc
from forms.product import ProductForm
from catalog.helpers import slugify
from werkzeug.utils import secure_filename
from datetime import datetime

login_manager = LoginManager(app)
login_manager.login_view = "site.login"
login_manager.session_protection = "strong"

site = Blueprint('site', __name__, template_folder='templates')


# common variables to the app
@app.context_processor
def inject():
    # fetch all the categories
    categories = Category.query.all()
    return dict(categories=categories)


@site.route('/')
def home():
    # fetch the last 16 products from the database
    products = Product.query.limit(16)

    return render_template(
        'home.html',
        products=products
    )


@site.route('/categories')
def categories():
    return render_template(
        'category/index.html'
    )


@site.route('/category/<slug>')
def category(slug):
    category_obj = Category.query.filter_by(slug=slug).first()

    products = Product.query.filter_by(category=category_obj).all()

    return render_template(
        'category/search.html',
        products=products, category=category_obj
    )


@site.route('/search')
def search():

    q = request.args.get('q', '')

    products = Product.query.filter(Product.title.like(
        '%'+q+'%')).from_self().all()

    return render_template(
        'search/search.html',
        products=products,
        term=q
    )


@site.route('/product/<int:product_id>/<product_slug>')
def product_view(product_id, product_slug):
    # fetch the product from the database
    product = Product.query.filter_by(id=product_id).first()

    return render_template(
        'products/view.html',
        product=product
    )


@site.route('/product/add', methods=["GET", "POST"])
@login_required
def product_add():
    categories = Category.query.all()

    product = Product()

    form = ProductForm(obj=product)

    # Set the categories to the form
    form.category_id.choices = [(c.id, c.name) for c in
                                Category.query.order_by('name')]

    if request.method == "POST":

        if form.validate():

            # populate Product obj with wtform data
            form.populate_obj(product)

            product.user_id = current_user.get_id()
            product.slug = slugify(product.title)

            f = form.picture.data

            # renames the file to prevent duplicated names
            filename = datetime.now().strftime(
                '%Y%m%d%H%M%S') + secure_filename(f.filename)

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"], 'uploads', filename
            )

            f.save(filepath)

            # @TODO Generate an image thumbnail

            product.picture = filename

            db_session.add(product)

            try:
                db_session.commit()
                flash('Nice! You just added your product to sell :D', 'success')
                redirect("/")
            except exc.SQLAlchemyError:
                db_session.rollback()
                flash('Error! There was an error trying to save your product',
                      'danger')

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(u"Error in the %s field - %s" % (
                        getattr(form, field).label.text,
                        error
                    ))

    return render_template(
        'products/add.html',
        categories=categories,
        form=form
    )


@site.route('/product/edit/<int:product_id>', methods=["GET", "POST"])
@login_required
def product_edit(product_id):
    categories = Category.query.all()

    product = Product.query.filter_by(id=product_id).first()

    # making sure that the current user owns the item
    if not current_user.get_id == product.user.id:
        return redirect("/")

    form = ProductForm(obj=product)

    # Set the categories to the form
    form.category_id.choices = [(c.id, c.name) for c in
                                Category.query.order_by('name')]

    if request.method == "POST":

        if form.validate():

            # populate Product obj with wtform data
            form.populate_obj(product)

            product.user_id = current_user.get_id()
            product.slug = slugify(product.title)

            # If user has uploaded another picture
            if hasattr(form.picture.data, 'filename'):
                f = form.picture.data

                # renames the file to prevent duplicated names
                filename = datetime.now().strftime(
                    '%Y%m%d%H%M%S') + secure_filename(f.filename)

                filepath = os.path.join(
                    app.config["UPLOAD_FOLDER"], 'uploads', filename
                )

                f.save(filepath)

                # @TODO Generate an image thumbnail
                product.picture = filename

            db_session.add(product)

            try:
                db_session.commit()
                flash('Nice! You just updated your product:D',
                      'success')
            except exc.SQLAlchemyError:
                db_session.rollback()
                flash('Error! There was an error trying to save your product',
                      'danger')

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(u"Error in the %s field - %s" % (
                        getattr(form, field).label.text,
                        error
                    ))

    return render_template(
        'products/add.html',
        categories=categories,
        form=form
    )


@site.route('/product/delete/<int:product_id>', methods=["GET", "POST"])
@login_required
def product_delete(product_id):
    product = Product.query.filter_by(id=product_id).first()

    # making sure that the current user owns the item
    if not current_user.get_id == product.user.id:
        return redirect("/")

    if product is not None:
        db_session.delete(product)
        db_session.commit()
        return redirect("/")
    else:
        return redirect("/")


@site.route('/account/items', methods=["GET", "POST"])
@login_required
def my_items():
    products = Product.query.filter_by(user_id=current_user.get_id()).all()

    return render_template('account/my_items.html', products=products)


@site.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('site.home'))
    google = get_google_auth()
    auth_url, state = google.authorization_url(
        app.config["AUTH_URI"], access_type='offline')
    session['oauth_state'] = state
    return render_template('auth/login.html', auth_url=auth_url)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


""" OAuth Session creation """


def get_google_auth(state=None, token=None):
    if token:
        return OAuth2Session(app.config['CLIENT_ID'], token=token)
    if state:
        return OAuth2Session(
            app.config['CLIENT_ID'],
            state=state,
            redirect_uri=app.config['REDIRECT_URI'])
    oauth = OAuth2Session(
        app.config['CLIENT_ID'],
        redirect_uri=app.config['REDIRECT_URI'],
        scope=app.config['SCOPE'])
    return oauth


@site.route('/auth/google')
def login_google():
    if current_user is not None and current_user.is_authenticated:
        return redirect(url_for('site.home'))

    if 'error' in request.args:
        if request.args.get('error') == 'access_denied':
            return 'You denied access.'
        return 'Error encountered.'

    if 'code' not in request.args and 'state' not in request.args:
        return redirect(url_for('login'))
    else:
        google = get_google_auth(state=session['oauth_state'])
        try:
            token = google.fetch_token(
                app.config['TOKEN_URI'],
                client_secret=app.config['CLIENT_SECRET'],
                authorization_response=request.url)
        except HTTPError:
            return 'HTTPError occurred.'

        google = get_google_auth(token=token)
        resp = google.get(app.config['USER_INFO'])

        if resp.status_code == 200:

            user_data = resp.json()
            email = user_data['email']
            user = User.query.filter_by(email=email).first()

            if user is None:
                user = User()
                user.email = email

            user.name = user_data['name']

            user.tokens = json.dumps(token)
            user.avatar = user_data['picture']
            user.provider = "google"

            db_session.add(user)
            db_session.commit()

            login_user(user)
            return redirect(url_for('site.home'))

        return 'Could not fetch your information.'


@site.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('site.home'))
