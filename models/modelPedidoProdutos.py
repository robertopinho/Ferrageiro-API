from banco import db
import hashlib
from config import config

class PedidoProdutos(db.Model):
    __tablename__: 'pedido_produtos'
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'), primary_key=True, nullable=False)
    produtos_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), primary_key=True,nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    valor = db.Column(db.Float, nullable=False)
    pedido = db.relationship('Pedido')
    produto = db.relationship('Produto')

    def to_json(self):
        json_pedido_produtos = {
            'pedido_id' : self.pedido_id,
            'produtos_id' : self.produtos_id,
            'quantidade' : self.quantidade,
            'valor' : self.valor,
        }
        return json_pedido_produtos
    
    @staticmethod
    def from_json(json_pedido_produtos):
        pedido_id = json_pedido_produtos.get('pedido_id')
        produtos_id = json_pedido_produtos.get('produtos_id')
        quantidade = json_pedido_produtos.get('quantidade')
        valor = json_pedido_produtos.get('valor')
        return PedidoProdutos(pedido_id=pedido_id, produtos_id=produtos_id,quantidade=quantidade,valor=valor)