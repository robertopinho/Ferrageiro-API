from banco import db
from datetime import datetime
    
class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data_compra = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    nome = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.String(200))
    imagem = db.Column(db.String(300))
    unidade = db.Column(db.String(2), nullable=False)
    quant = db.Column(db.Integer, nullable=False)
    quant_minima = db.Column(db.Integer, nullable=False)
    valor_compra = db.Column(db.Float, nullable=False)
    porcentagem = db.Column(db.Integer)
    valor_venda = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Float)
    fornecedor_id = db.Column(db.Integer, db.ForeignKey(
        'fornecedores.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey(
        'marcas.id'), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey(
        'categorias.id'), nullable=False)
    destaque = db.Column(db.String(1))

    fornecedor = db.relationship('Fornecedor')
    marca = db.relationship('Marca')
    categoria = db.relationship('Categoria')

    def to_json(self):
        json_produtos = {
            'id': self.id,
            'data_compra': self.data_compra,
            'nome': self.nome,
            'descricao': self.descricao,
            'imagem': self.imagem,
            'unidade': self.unidade,
            'quant': self.quant,
            'quant_minima': self.quant_minima,
            'valor_compra': self.valor_compra,
            'porcentagem': self.porcentagem,
            'valor_venda': self.valor_venda,
            'peso': self.peso,
            'fornecedor_id': self.fornecedor_id,
            'marca_id': self.marca_id,
            'categoria_id': self.categoria_id,
            'destaque': self.destaque
        }
        return json_produtos

    @staticmethod
    def from_json(json_produtos):
        id = json_produtos.get('id')
        data_compra = json_produtos.get('data_compra')
        nome = json_produtos.get('nome')
        descricao = json_produtos.get('descricao')
        imagem = json_produtos.get('imagem')
        unidade = json_produtos.get('unidade')
        quant = json_produtos.get('quant')
        quant_minima = json_produtos.get('quant_minima')
        valor_compra = json_produtos.get('valor_compra')
        porcentagem = json_produtos.get('porcentagem')
        valor_venda = json_produtos.get('valor_venda')
        peso = json_produtos.get('peso')
        fornecedor_id = json_produtos.get('fornecedor_id')
        marca_id = json_produtos.get('marca_id')
        categoria_id = json_produtos.get('categoria_id')
        destaque = json_produtos.get('destaque')

        return Produto(id=id, data_compra=data_compra,nome=nome, descricao=descricao, imagem=imagem, unidade=unidade, quant=quant,
                       quant_minima=quant_minima, valor_compra=valor_compra, porcentagem=porcentagem, valor_venda=valor_venda,
                       peso=peso, fornecedor_id=fornecedor_id, marca_id=marca_id, categoria_id=categoria_id, destaque=destaque)
