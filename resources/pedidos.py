from flask import Blueprint, jsonify, request
from banco import db
from models.modelPedido import Pedido
from flask_cors import CORS

pedido = Blueprint('pedido', __name__)

@pedido.route('/pedido', methods=['POST'])
def adicionar():
    pedidos = Pedido.from_json(request.json)
    db.session.add(pedidos)
    db.session.commit()
    print(pedidos.to_json())
    return jsonify(pedidos.to_json()), 201

@pedido.route('/pedido')
def listagem():
    pedido = Pedido.query.order_by(Pedido.id).all()
    return jsonify([pedido.to_json() for pedido in pedido])
    
@pedido.route('/pedidos', methods=['POST'])
def addAll():
    for x in request.json:
        pedidos = Pedido.from_json(x)
        db.session.add(pedidos)
        db.session.commit()
        print(pedidos)
    return jsonify([x for x in request.json]), 201