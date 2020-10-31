from banco import db
import hashlib
from config import config

class Uf(db.Model):
    __tablename__: 'uf'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sigla = db.Column(db.String(2), nullable=False)

    def to_json(self):
        json_uf = {
        'id': self.id,
        'sigla': self.sigla,
        }
        return json_uf

    @staticmethod
    def from_json(json_uf):
        id = json_uf.get('id')
        sigla = json_uf.get('sigla')
        return Uf(id=id, sigla=sigla)