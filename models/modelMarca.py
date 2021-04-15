from banco import db
from sqlalchemy.orm import relationship
class Marca(db.Model):
    __tablename__ = 'marcas'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)

    produtos = relationship('Produto', secondary='produto_marca')

    def to_json(self):
        json_marcas = {
            'id': self.id,
            'nome': self.nome
        }
        return json_marcas

    @staticmethod
    def from_json(json_marcas):
        nome = json_marcas.get('nome')
        return Marca(nome=nome)

