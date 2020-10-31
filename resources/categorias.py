from flask import Blueprint, jsonify, request
from banco import db
from models.modelCategoria import Categoria
from flask_cors import CORS

categorias = Blueprint('categorias', __name__)


@categorias.route('/categorias', methods=['POST'])
def adicionar():
    categoria = Categoria.from_json(request.json)
    db.session.add(categoria)
    db.session.commit()
    return jsonify(categoria.to_json()), 201

@categorias.route('/listacategorias')
def listagem():
    listacategorias = Categoria.query.order_by(Categoria.nome).all()
    return jsonify([listacategoria.to_json() for listacategoria in listacategorias])

@categorias.route('/listacategorias/<int:id>', methods=['DELETE'])
def excluir(id):
    Categoria.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify  ({'id':id, 'message':'Categoria Excluida com sucesso'}),200
    
