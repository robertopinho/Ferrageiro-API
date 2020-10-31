from flask import Blueprint, jsonify, request
from banco import db
from flask_cors import CORS
from models.modelCarrinho import Carrinho
carrinho = Blueprint('carrinho', __name__)

@carrinho.route('/carrinho')
def listagem():
    carrinho = Carrinho.query.order_by(Carrinho.id).all()
    return jsonify([carrinho.to_json() for carrinho in carrinho])

@carrinho.route('/carrinho', methods=['POST'])
def adicionar():
    carrinho = Carrinho.from_json(request.json)
    db.session.add(carrinho)
    db.session.commit()
    return jsonify(carrinho.to_json()), 201

