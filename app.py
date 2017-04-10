from flask import Flask, render_template, jsonify
from database import init_db

app = Flask(__name__)

# init the database
init_db()


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)