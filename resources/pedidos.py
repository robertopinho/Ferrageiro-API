from flask import Blueprint, jsonify, request
from banco import db
from models.modelPedido import Pedido
from flask_cors import CORS

pedido = Blueprint('pedido', __name__)

@pedido.route('/pedido', methods=['POST'])
def adicionar():
    pedido = Pedido.from_json(request.json)
    db.session.add(pedido)
    db.session.commit()
    return jsonify(pedido.to_json()), 201

@pedido.route('/pedido')
def listagem():
    pedido = Pedido.query.order_by(Pedido.id).all()
    return jsonify([pedido.to_json() for pedido in pedido])
 