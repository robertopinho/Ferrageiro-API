from banco import db
from sqlalchemy.orm import relationship
class Produto_categoria(db.Model):
    __tablename__: 'produto_categoria'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    
    produtos = relationship('Produto')
    categorias = relationship('Categoria')

