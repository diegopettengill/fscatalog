from flask import Flask, render_template

from database import init_db

app = Flask(__name__)

# app.config.from_pyfile('config.py')



# init the database
init_db()

import catalog.views
@app.route("/")
def index_as():
    return render_template("menu.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
