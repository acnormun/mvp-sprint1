from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
agrupamento_bp = Blueprint('agrupamento', __name__)

class Agrupamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantidade_de_toras = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)

@agrupamento_bp.route('/cadastrar_agrupamento', methods=['POST'])
def cadastrar_agrupamento():
    data = request.get_json()
    novo_agrupamento = Agrupamento(
        id=data['id'],
        quantidade_de_toras=data['quantidade_de_toras'],
        peso=data['peso']
    )
    db.session.add(novo_agrupamento)
    db.session.commit()
    return jsonify({"message": "Agrupamento cadastrado com sucesso!"}), 200

@agrupamento_bp.route('/editar_agrupamento/<int:id>', methods=['PUT'])
def editar_agrupamento(id):
    data = request.get_json()
    agrupamento = Agrupamento.query.get_or_404(id)
    agrupamento.quantidade_de_toras = data.get('quantidade_de_toras', agrupamento.quantidade_de_toras)
    agrupamento.peso = data.get('peso', agrupamento.peso)
    db.session.commit()
    return jsonify({"message": "Agrupamento atualizado com sucesso!"}), 200

@agrupamento_bp.route('/buscar_agrupamentos', methods=['GET'])
def buscar_agrupamentos():
    agrupamentos = Agrupamento.query.all()
    return jsonify([
        {"id": a.id, "quantidade_de_toras": a.quantidade_de_toras, "peso": a.peso}
        for a in agrupamentos
    ]), 200

@agrupamento_bp.route('/deletar_agrupamento/<int:id>', methods=['DELETE'])
def deletar_agrupamento(id):
    agrupamento = Agrupamento.query.get_or_404(id)
    db.session.delete(agrupamento)
    db.session.commit()
    return jsonify({"message": "Agrupamento deletado com sucesso!"}), 200
