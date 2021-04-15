from banco import db
from sqlalchemy.orm import relationship

class Produto_marca(db.Model):
    __tablename__: 'produto_marca'
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'))
    marca_id = db.Column(db.Integer, db.ForeignKey('marcas.id'))
    
    produtos = relationship('Produto')
    marcas = relationship('Marca')