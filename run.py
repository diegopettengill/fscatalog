from catalog import app
from database import init_db
from OpenSSL import SSL
import os

context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file(os.path.join(os.path.dirname(__file__), 'ssl.key'))
context.use_certificate_file(os.path.join(os.path.dirname(__file__),
                                          'ssl.cert'))

# init the database
init_db()

# configure ssl, required for oauth
# context = (cer, key)
app.run(host='0.0.0.0', debug=True, ssl_context=context)
