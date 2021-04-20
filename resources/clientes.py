from flask import Blueprint, jsonify, request
from banco import db
from models.modelCliente import Cliente
from config import config
import hashlib
from flask_jwt_extended import create_access_token, jwt_required, get_raw_jwt
from blacklist import blacklist

clientes = Blueprint('clientes', __name__)

@clientes.route('/clientes')
def listagem():
    clientes = Cliente.query.order_by(Cliente.id).all()
    return jsonify([cliente.to_json() for cliente in clientes])

@clientes.route('/clientes/<int:id>')
def detalhes(id):
    detalhes = Cliente.query.order_by(Cliente.id).filter(Cliente.id == id)
    return jsonify([detalhes.to_json() for detalhes in detalhes])

@clientes.route('/clientes', methods=['POST'])
def adicionar():
    cliente = Cliente.from_json(request.json)
    db.session.add(cliente)
    db.session.commit()
    return jsonify(cliente.to_json()), 201


@clientes.route('/clientes/<int:id>', methods=['DELETE'])
def excluir(id):
    Cliente.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'id': id, 'message': 'Cliente excluído com sucesso'}), 200

# @clientes.route('/clientes/<int:id>', methods=['PUT'])
# def alterar(id):
#     cliente = Cliente.query.get_or_404(id)
#     db.session.add(cliente)
#     db.session.commit()
#     return jsonify(cliente.to_json()), 204


@clientes.route('/clientes/<int:id>', methods=['PUT'])
def alterar(id):
    cliente = Cliente.query.get_or_404(id)
    cliente.cidade_id = request.json['cidade_id']
    cliente.cpf = request.json['cpf']
    cliente.email = request.json['email']
    cliente.endereco_bairro = request.json['endereco_bairro']
    cliente.endereco_complemento = request.json['endereco_complemento']
    cliente.endereco_logradouro = request.json['endereco_logradouro']
    cliente.endereco_numero = request.json['endereco_numero']
    cliente.endereco_tipo = request.json['endereco_tipo']
    cliente.nome = request.json['nome']
    cliente.telefone = request.json['telefone']
    cliente.uf_id = request.json['uf_id']
    db.session.add(cliente)
    db.session.commit()
    return jsonify(cliente.to_json()), 204


@clientes.route('/entrar', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    senha = request.json.get('senha', None)
    if not email:
        return jsonify({"msg": "Missing email parameter"}), 400
    if not senha:
        return jsonify({"msg": "Missing senha parameter"}), 400

    senha += config.SALT
    senha_md5 = hashlib.md5(senha.encode()).hexdigest()

    cliente = Cliente.query \
        .filter(Cliente.email == email) \
        .filter(Cliente.senha == senha_md5) \
        .first()

    if cliente:
        nome = cliente.nome.split(' ')
        access_token = create_access_token(identity=email)
        return jsonify({"user": nome[0], "access_token": access_token}), 200
    else:
        return jsonify({"user": None, "access_token": None}), 200


@clientes.route('/logout')
@jwt_required
def logout():
    jti = get_raw_jwt()['jti']
    blacklist.add(jti)
    return jsonify({"msg": "Successfully logged out"}), 200
