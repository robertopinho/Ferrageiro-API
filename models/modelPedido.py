from banco import db
from datetime import datetime
class Pedido(db.Model):
    __tablename__ = 'pedido'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    data_compra = db.Column(db.DateTime, nullable=False, default=datetime.now)
    data_entrega = db.Column(db.DateTime, nullable=False, default=datetime.now)
    #valor_entrega = db.Column(db.DateTime, nullable=False, default=datetime.now)
    desconto = db.Column(db.Float)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), nullable=False)
    observacao = db.Column(db.String(200))
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    clientes = db.relationship('Cliente')
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    usuarios = db.relationship('Usuario')

    
    def to_json(self):
        json_pedido = {
            'id': self.id,
            'data_compra': self.data_compra,
            'data_entrega': self.data_entrega,
            'desconto': self.desconto,
            'valor': self.valor,
            'status': self.status,
            'observacao': self.observacao,
            'id_cliente': self.id_cliente , 
            'id_usuario': self.id_usuario , 
        }
        return json_pedido

    @staticmethod
    def from_json(json_pedido):
        id = json_pedido.get('id')
        data_compra = json_pedido.get('data_compra')
        data_entrega = json_pedido.get('data_entrega')
        id_cliente = json_pedido.get('id_cliente')
        desconto = json_pedido.get('desconto')
        status = json_pedido.get('status')
        observacao = json_pedido.get('observacao')
        valor = json_pedido.get('valor')
        id_usuario = json_pedido.get('id_usuario')
    

        return Pedido(id=id, data_compra=data_compra, data_entrega=data_entrega, id_cliente=id_cliente, desconto=desconto,status=status,observacao=observacao, valor=valor, id_usuario=id_usuario)