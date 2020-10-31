from banco import db
import hashlib
from config import config

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(32), nullable=False)
    telefone = db.Column(db.String(11))
    enderecoLogradouro = db.Column(db.String(100))
    enderecoBairro = db.Column(db.String(40))

    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id'), nullable=False )
    uf_id = db.Column(db.Integer, db.ForeignKey('uf.id'), nullable=False)
    enderecoNumero = db.Column(db.Integer)
    enderecoComplemento = db.Column(db.String(60))
    enderecoTipo = db.Column(db.String(20))

    cidade = db.relationship('Cidade')
    uf = db.relationship('Uf')
      
    def to_json(self):
        json_clientes = {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'enderecoLogradouro': self.enderecoLogradouro,
            'enderecoBairro': self.enderecoBairro,
            'cidade_id': self.cidade_id,
            'uf_id': self.uf_id,
            'enderecoNumero': self.enderecoNumero,
            'enderecoComplemento': self.enderecoComplemento,
            'enderecoTipo' : self.enderecoTipo,
        }
        return json_clientes

    @staticmethod
    def from_json(json_clientes):
        id = json_clientes.get('id')
        nome = json_clientes.get('nome')
        cpf = json_clientes.get('cpf')
        email = json_clientes.get('email')
        senha = json_clientes.get('senha') + config.SALT
        senha_md5 = hashlib.md5(senha.encode()).hexdigest()
        telefone = json_clientes.get('telefone')
        enderecoLogradouro = json_clientes.get('enderecoLogradouro')
        enderecoBairro = json_clientes.get('enderecoBairro')
        cidade_id = json_clientes.get('cidade_id')
        uf_id = json_clientes.get('uf_id')
        enderecoNumero = json_clientes.get('enderecoNumero')
        enderecoComplemento = json_clientes.get('enderecoComplemento')
        enderecoTipo = json_clientes.get('enderecoTipo')
        return Cliente(id=id, nome=nome, cpf=cpf, email=email, senha=senha_md5, telefone=telefone,
                       enderecoLogradouro=enderecoLogradouro, enderecoBairro=enderecoBairro,
                        cidade_id=cidade_id,uf_id=uf_id, enderecoNumero=enderecoNumero,
                         enderecoComplemento=enderecoComplemento, enderecoTipo=enderecoTipo)
