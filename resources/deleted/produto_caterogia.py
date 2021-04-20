from flask import Blueprint, jsonify, request
from banco import db
from models.modelProduto_categoria import Produto_categoria
from flask_cors import CORS

produto_categoria = Blueprint('produto_categoria', __name__)
