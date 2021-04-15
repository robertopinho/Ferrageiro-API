from flask import Flask, jsonify, Blueprint
from config import config
from banco import db
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from resources.produtos import produtos
from resources.fornecedores import fornecedores
from resources.marcas import marcas
from resources.categorias import categorias
from resources.usuarios import usuarios
from resources.clientes import clientes
from resources.pedidos import pedido
from resources.uf import uf
from resources.carrinho import carrinho
from resources.cidades import cidade
from resources.produto_caterogia import produto_categoria
from resources.produto_fornecedor import produto_fornecedor
from resources.produto_marca import produto_marca



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
jwt = JWTManager(app)

CORS(app)
app.register_blueprint(categorias)
app.register_blueprint(produtos)
app.register_blueprint(marcas)
app.register_blueprint(fornecedores)
app.register_blueprint(usuarios)
app.register_blueprint(clientes)
app.register_blueprint(uf)
app.register_blueprint(cidade)
app.register_blueprint(carrinho)
app.register_blueprint(pedido)
app.register_blueprint(produto_marca)
app.register_blueprint(produto_fornecedor)
app.register_blueprint(produto_categoria)


@app.route('/')
def raiz():
    html = '<h2>Ferrageiro - Processo Interno</h2><p>API do sistema Ferrageiro<p>'
    return html

@app.route('/criadb')
def criadb():
    db.create_all()
    return "Ok! Tabelas criadas com sucesso"

@app.route('/restartdb')
def restartdb():
    db.drop_all()
    db.create_all()
    return "Tabelas excluidas! \nTabelas Criadas novamente!"

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return jti in blacklist

if __name__ == '__main__':
    app.run(debug=True)
