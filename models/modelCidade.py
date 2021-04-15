from banco import db
import hashlib
from config import config

class Cidade(db.Model):
    __tablename__: 'cidades'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(45))
    uf_id = db.Column(db.Integer, db.ForeignKey('uf.id'), nullable=False)
    uf = db.relationship('Uf')
    
    
    def to_json(self):
        json_cidades = {
            'id' : self.id,
            'nome' : self.nome,
            'uf_id': self.uf_id,
        }
        return json_cidades
    
    @staticmethod
    def from_json(json_cidades):
        id = json_cidades.get('id')
        nome = json_cidades.get('nome')
        uf_id = json_cidades.get('uf_id')
        return Cidade(id=id, nome=nome, uf_id=uf_id)