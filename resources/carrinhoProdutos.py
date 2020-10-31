from flask import Blueprint, jsonify, request
from banco import db
from models.modelCarrinhoProdutos import CarrinhoProdutos
from flask_cors import CORS

carrinho_produtos = Blueprint('carrinho_produtos', __name__)

@carrinho_produtos.route('/carrinho_produtos', methods=['POST'])
def adicionar():
    carrinho_produtos = CarrinhoProdutos.from_json(request.json)
    db.session.add(carrinho_produtos)
    db.session.commit()
    return jsonify(carrinho_produtos.to_json()), 201


