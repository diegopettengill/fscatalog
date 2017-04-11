from flask import Flask

from database import init_db

app = Flask(__name__)

app.config.from_pyfile('config.py')

# init the database
init_db()



@app.route("/")
def index():
    return "CARALHO"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
