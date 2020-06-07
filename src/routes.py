from flask import request, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Order
from flask import jsonify


@app.route('/', methods=['GET'])
def healthcheck():
    return make_response(jsonify({"health": "ok"}), 200)


@app.route("/order", methods=['POST'])
def add():
    order: Order = request.json
    if order:
        neworder = Order(accountId=order["accountId"],
                         productId=order["productId"],
                         productName=order["productName"],
                         productBrand=order["productBrand"],
                         created=dt.now(),
                         amount=order["amount"],
                         status=order["status"],
                         quantity=order["quantity"])
        db.session.add(neworder)
        db.session.commit()
        return make_response(jsonify(data=[e.serialize() for e in Order.query.all()]), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/order", methods=['GET'])
def get():
    data = Order.query.all()
    if data:
        return make_response(jsonify(data=[e.serialize() for e in Order.query.all()]), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/order/<int:orderid>", methods=['GET'])
def findbyid(orderid):
    if orderid:
        order = Order.query.filter(Order.orderId == orderid).first()
        if order:
            return make_response(jsonify(data=order.serialize()), 200)
        return make_response(jsonify({"resp": "Not found"}), 404)
    return make_response(jsonify({"resp": "Not found"}), 404)


@app.route("/order", methods=['PUT'])
def update():
    order: Order = request.json
    if order:
        existing_order: Order = Order.query.filter(Order.orderId == order["orderId"]).first()
        if not existing_order:
            return make_response(jsonify({"order": order["orderId"]}), 404)
        existing_order.status = order["status"]
        db.session.commit()
        return make_response(jsonify(data=existing_order.serialize()), 200)
    return make_response(jsonify({"resp": "Not found"}), 404)
