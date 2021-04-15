from banco import db
from sqlalchemy.orm import relationship

class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
       
    # produtos = relationship('Produto', secondary='produto_categoria')

    def to_json(self):
        json_categoria = {
            'id': self.id,
            'nome': self.nome
        }
        return json_categoria

    @staticmethod
    def from_json(json_categoria):
        nome = json_categoria.get('nome')
        return Categoria(nome=nome)
