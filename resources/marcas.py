from flask import Blueprint, jsonify, request
from banco import db
from models.modelMarca import Marca
from flask_cors import CORS

marcas = Blueprint('marcas', __name__)


@marcas.route('/marcas', methods=['POST'])
def adicionar():
    marca = Marca.from_json(request.json)
    db.session.add(marca)
    db.session.commit()
    return jsonify(marca.to_json()), 201


@marcas.route('/listamarcas')
def listagem():
    listamarcas = Marca.query.order_by(Marca.nome).all()
    return jsonify([listamarca.to_json() for listamarca in listamarcas])


@marcas.route('/listamarcas/<int:id>', methods=['DELETE'])
def excluir(id):
    Marca.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Marca Excluida com sucesso'}),200