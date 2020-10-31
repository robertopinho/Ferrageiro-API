from banco import db
import hashlib
from config import config

class CarrinhoProdutos(db.Model):
    __tablename__ = 'carrinho_produtos'
    carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'), primary_key=True , nullable=False)
    produtos_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), primary_key=True ,nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    desconto = db.Column(db.Float)
    valor = db.Column(db.Float, nullable=False)
    produto = db.relationship('Produto')
    carrinho = db.relationship('Carrinho')


    def to_json(self):
        json_carrinho_produtos = {
            'carrinho_id' : self.carrinho_id,
            'produtos_id' : self.produtos_id,
            'quantidade' : self.quantidade,
            'desconto' : self.desconto,
            'valor' : self.valor, 
        }
        return json_carrinho_produtos

    @staticmethod
    def from_json(json_carrinho_produtos):
        carrinho_id = json_carrinho_produtos.get('carrinho_id')
        produtos_id = json_carrinho_produtos.get('produtos_id')
        quantidade = json_carrinho_produtos.get('quantidade')
        desconto = json_carrinho_produtos.get('desconto')
        valor = json_carrinho_produtos.get('valor')
        return CarrinhoProdutos(carrinho_id=carrinho_id, produtos_id=produtos_id, quantidade=quantidade, desconto=desconto, valor=valor)