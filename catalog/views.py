from flask import render_template, jsonify
from app import app


@app.route("/ca")
def index():
    return render_template("menu.html")
