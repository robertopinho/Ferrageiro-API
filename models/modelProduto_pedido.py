from banco import db
import hashlib
from config import config
from sqlalchemy.orm import relationship

class Produto_pedido(db.Model):
    __tablename__: 'produto_pedido'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedido.id'))
    
    produtos = relationship('Produto')
    pedidos = relationship('Pedido')