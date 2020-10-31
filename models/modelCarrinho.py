from banco import db
from datetime import datetime

class Carrinho(db.Model):

    __tablename__ = 'carrinho'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    valor_total = db.Column(db.Float, nullable=False)
    desconto = db.Column(db.Float, nullable=False)
    quant_compra = db.Column(db.Integer, nullable=False)
    fechado = db.Column(db.Boolean, nullable=False)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    
    cliente = db.relationship('Cliente')

    def to_json(self):
        json_carrinho    = {
            'id' : self.id,
            'data' : self.data,
            'id_cliente' : self.id_cliente,
            'valor_total' : self.valor_total,
            'desconto' : self.desconto,
            'fechado' : self.fechado,
            'quant_compra' : self.quant_compra
        }
        return json_carrinho    

    @staticmethod
    def from_json(json_carrinho ):
        id = json_carrinho.get('id')
        data = json_carrinho.get('data')
        id_cliente = json_carrinho.get('id_cliente')
        valor_total = json_carrinho.get('valor_total')
        fechado = json_carrinho.get('fechado')
        desconto = json_carrinho.get('desconto')
        quant_compra = json_carrinho.get('quant_compra')

        return Carrinho(id=id,data=data,id_cliente=id_cliente, valor_total=valor_total,fechado=fechado, desconto=desconto,quant_compra=quant_compra)

