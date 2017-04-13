from catalog import app
from database import init_db

# init the database
init_db()

app.run(host='0.0.0.0', debug=True)