from flask import Blueprint, jsonify, request
from banco import db
from flask_cors import CORS
from models.modelCidade import Cidade 
cidade = Blueprint('cidade', __name__)

@cidade.route('/cidade', methods=['POST'])
def adicionar():
    cidade = Cidade.from_json(request.json)
    db.session.add(cidade)
    db.session.commit()
    return jsonify(cidade.to_json()), 201

@cidade.route('/cidade')
def listagem():
    cidade = Cidade.query.order_by(Cidade.nome).all()
    return jsonify([cidade.to_json() for cidade in cidade])