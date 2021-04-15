from flask import Blueprint, jsonify, request
from banco import db
from models.modelProduto_fornecedor import Produto_fornecedor
from flask_cors import CORS

produto_fornecedor = Blueprint('produto_fornecedor', __name__)
