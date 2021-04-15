from flask import Blueprint, jsonify, request
from banco import db
from models.modelCarrinho import Carrinho
from flask_cors import CORS

carrinho = Blueprint('carrinho', __name__)

     
@carrinho.route('/carrinho', methods=['POST'])
def addAll():
    for x in request.json:
        carrinho = Carrinho.from_json(x)
        db.session.add(carrinho)
        db.session.commit()
        print(carrinho)
    return jsonify([x for x in request.json]), 201



@carrinho.route('/carrinho')
def listagem():
    carrinho = Carrinho.query.order_by(produto_id).all()
    return jsonify([carrinho.to_json() for carrinho in carrinho])
    