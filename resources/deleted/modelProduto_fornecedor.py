from banco import db
from sqlalchemy.orm import relationship
class Produto_fornecedor(db.Model):
    __tablename__: 'produto_fornecedor'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    fornecedor_id = db.Column(db.Integer, db.ForeignKey('fornecedores.id'))
    
    produtos = relationship('Produto')
    fornecedores = relationship('Fornecedor')