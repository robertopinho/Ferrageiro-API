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
    endereco_logradouro = db.Column(db.String(100))
    endereco_bairro = db.Column(db.String(40))
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id'), nullable=False )
    endereco_numero = db.Column(db.Integer)
    endereco_complemento = db.Column(db.String(60))
    endereco_tipo = db.Column(db.String(20))

    cidade = db.relationship('Cidade')
      
    def to_json(self):
        json_clientes = {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'endereco_logradouro': self.endereco_logradouro,
            'endereco_bairro': self.endereco_bairro,
            'cidade_id': self.cidade_id,
   
            'endereco_numero': self.endereco_numero,
            'endereco_complemento': self.endereco_complemento,
            'endereco_tipo' : self.endereco_tipo,
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
        endereco_logradouro = json_clientes.get('endereco_logradouro')
        endereco_bairro = json_clientes.get('endereco_bairro')
        cidade_id = json_clientes.get('cidade_id')
        
        endereco_numero = json_clientes.get('endereco_numero')
        endereco_complemento = json_clientes.get('endereco_complemento')
        endereco_tipo = json_clientes.get('endereco_tipo')
        return Cliente(id=id, nome=nome, cpf=cpf, email=email, senha=senha_md5, telefone=telefone,
                       endereco_logradouro=endereco_logradouro, endereco_bairro=endereco_bairro,
                        cidade_id=cidade_id, endereco_numero=endereco_numero,
                         endereco_complemento=endereco_complemento, endereco_tipo=endereco_tipo)
