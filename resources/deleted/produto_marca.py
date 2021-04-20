from flask import Blueprint, jsonify, request
from banco import db
from models.modelProduto_marca import Produto_marca
from flask_cors import CORS

produto_marca = Blueprint('produto_marca', __name__)
