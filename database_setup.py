from catalog import app
from database import init_db
from OpenSSL import SSL
import os

# init the database
init_db()