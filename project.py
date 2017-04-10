from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurant_menu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/restaurants/<int:restaurant_id>/")
def restaurant_menu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template("menu.html", restaurant=restaurant, items=items)


@app.route("/restaurant/<int:restaurant_id>/new/")
def new_menu_item(restaurant_id):
    return "page for new menu item"


@app.route("/restaurant/<int:restaurant_id>/<int:item_id>/edit")
def edit_menu_item(restaurant_id, item_id):
    return "page for editing item"


@app.route("/restaurant/<int:restaurant_id>/<int:item_id>/delete")
def delete_menu_item(restaurant_id, item_id):
    return "page for delete an item"


# API ROUTES
@app.route("/api/itens/<int:restaurant_id>/")
def api_menu_itens(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return jsonify(MenuItem=[i.serialize for i in items])


# single item route
@app.route("/api/item/<int:item_id>/")
def api_menu_item(item_id):
    item = session.query(MenuItem).filter_by(id=item_id).one()
    return jsonify(MenuItem=item.serialize)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
