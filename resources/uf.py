from flask import Blueprint, jsonify, request
from banco import db
from flask_cors import CORS
from models.modelUF import Uf
uf = Blueprint('uf', __name__)

@uf.route('/uf', methods=['POST'])
def adicionar():
    uf = Uf.from_json(request.json)
    db.session.add(uf)
    db.session.commit()
    return jsonify(uf.to_json()), 201

@uf.route('/uf')
def listagem():
    uf = Uf.query.order_by(Uf.sigla).all()
    return jsonify([uf.to_json() for uf in uf])