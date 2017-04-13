from flask import Flask, send_from_directory

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'catalog/uploads/'

# Registering the app blueprints
from catalog.api.routes import api
from catalog.site.routes import site

app.register_blueprint(site)
app.register_blueprint(api, url_prefix='/api')