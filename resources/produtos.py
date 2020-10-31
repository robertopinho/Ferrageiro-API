from flask import Blueprint, jsonify, request
from banco import db
from models.modelProduto import Produto
from flask_cors import CORS

produtos = Blueprint('produtos', __name__)

# @produtos.route('/produto', methods=['POST'])
# def adicionar():
#     produto = Produto.from_json(request.json)
#     db.session.add(produto)
#     db.session.commit()
#     return jsonify(produto.to_json()), 201
    
@produtos.route('/produtos', methods=['POST'])
def adicionar():
    for x in request.json:
        produto = Produto.from_json(x)
        db.session.add(produto)
        db.session.commit()
    return jsonify([x for x in request.json]), 201

@produtos.route('/produtos/<int:id>', methods=['DELETE'])
def excluir(id):
    Produto.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Produto excluído com sucesso'}), 200

@produtos.route('/produtos')
def listagem():
    produtos = Produto.query.order_by(Produto.nome).all()
    return jsonify([produto.to_json() for produto in produtos])

@produtos.route('/produtos/<int:id>')
def produto(id):
    produtos = Produto.query.order_by(Produto.id).filter(Produto.id == id).one();
    return jsonify(produtos.to_json())

@produtos.route('/destaques')
def destaques():
    produtos = Produto.query.order_by(Produto.id).filter(
        Produto.destaque == "⭐").all()

    return jsonify([produto.to_json() for produto in produtos])

@produtos.route('/produtos/destacar/<int:id>', methods=['PUT'])
def destacar(id):
    produto = Produto.query.get_or_404(id)
    produto = Produto.query.order_by(Produto.id).filter(Produto.id == id).one()
    if(produto.destaque == ""):
        produto.destaque = "⭐"
        db.session.add(produto)
        db.session.commit()
        return jsonify({"msg": "Destaque Adicionado!"}), 200
    else:
        produto.destaque = ""
        db.session.add(produto)
        db.session.commit()
        return jsonify({"msg": "Destaque Removido!"}), 200

@produtos.route('/busca/<produto>')
def busca(produto):
    produtos = Produto.query.order_by(Produto.id).filter(
        Produto.nome.like(f'%{produto}%')).all()
    if(len(produtos) == 0):
        return jsonify({"msg": "Produto não encontrado!"})
    else:
        return jsonify([produto.to_json() for produto in produtos]), 200

