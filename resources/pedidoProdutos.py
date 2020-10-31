from flask import Blueprint, jsonify, request
from banco import db
from models.modelPedidoProdutos import PedidoProdutos
from flask_cors import CORS

pedido_produtos = Blueprint('pedido_produtos', __name__)