from banco import db
from sqlalchemy.orm import relationship


class Fornecedor(db.Model):
    __tablename__ = 'fornecedores'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    cnpj = db.Column(db.String(14), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    representante = db.Column(db.String(30), nullable=False)
    telefone_representante = db.Column(db.String(15), nullable=False)
    email_representante = db.Column(db.String(60), nullable=False)
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id') )
    cidade = db.relationship('Cidade')

    # produtos = relationship('Produto', secondary='produto_fornecedor')
    
    
    def to_json(self):
        json_fornecedor = {
            'id': self.id,
            'nome': self.nome,
            'cnpj': self.cnpj,
            'telefone': self.telefone,
            'email': self.email,
            'representante': self.representante,
            'telefone_representante': self.telefone_representante,
            'email_representante': self.email_representante,
            'cidade_id' : self.cidade_id,

        }
        return json_fornecedor

    @staticmethod
    def from_json(json_fornecedor):
        nome = json_fornecedor.get('nome')
        cnpj = json_fornecedor.get('cnpj')
        telefone = json_fornecedor.get('telefone')
        email = json_fornecedor.get('email')
        representante = json_fornecedor.get('representante')
        telefone_representante = json_fornecedor.get('telefone_representante')
        email_representante = json_fornecedor.get('email_representante')
        cidade_id = json_fornecedor.get('cidade_id')
        return Fornecedor(nome=nome, cnpj=cnpj, telefone=telefone, email=email, representante=representante,
                          telefone_representante=telefone_representante, email_representante=email_representante, cidade_id=cidade_id)


