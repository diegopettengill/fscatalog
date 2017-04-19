from flask import Flask, send_from_directory
from site import middlewares


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'catalog/uploads/'

# middlewares
app.wsgi_app = middlewares.AppMiddleware(app.wsgi_app)

# Registering the app blueprints
from catalog.api.routes import api
from catalog.site.routes import site

app.register_blueprint(site)
# app.register_blueprint(category)
app.register_blueprint(api, url_prefix='/api')
