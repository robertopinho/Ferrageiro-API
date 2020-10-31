from flask import Blueprint, jsonify, request
from banco import db
from models.modelFornecedor import Fornecedor
from flask_cors import CORS

fornecedores = Blueprint('fornecedores', __name__)


@fornecedores.route('/fornecedores', methods=['POST'])
def adicionar():
    fornecedor = Fornecedor.from_json(request.json)
    db.session.add(fornecedor)
    db.session.commit()
    return jsonify(fornecedor.to_json()), 201

@fornecedores.route('/detalhesfornecedor/<int:id>')
def detalhes(id):
    fornecedor = Fornecedor.query.order_by(Fornecedor.id).filter(Fornecedor.id == id).one();
    return jsonify(fornecedor.to_json())


@fornecedores.route('/listafornecedores')
def listagem():
    listafornecedores = Fornecedor.query.order_by(Fornecedor.nome).all()
    return jsonify([listafornecedor.to_json() for listafornecedor in listafornecedores])

@fornecedores.route('/listafornecedores/<int:id>', methods=['DELETE'])
def excluir(id):
    Fornecedor.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id':id, 'message': "Fornecedor excluido com sucesso."}),200

