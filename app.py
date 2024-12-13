from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from swagger_config import setup_swagger
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agrupamentos.db'
db = SQLAlchemy(app)

CORS(app)

# Configuração do Swagger
setup_swagger(app)

# Modelo do banco de dados
class Agrupamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantidade_de_toras = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)

# Criação do banco de dados dentro do contexto da aplicação
with app.app_context():
    db.create_all()

# Rotas
@app.route('/cadastrar_agrupamento', methods=['POST'])
def cadastrar_agrupamento():
    """
    Cadastrar um novo agrupamento
    ---
    tags:
      - Agrupamentos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            id:
              type: integer
              description: Id do agrupamento
              example: 1
            quantidade_de_toras:
              type: integer
              description: Quantidade de toras no agrupamento
              example: 10
            peso:
              type: number
              format: float
              description: Peso total do agrupamento em kg
              example: 1200.5
    responses:
      200:
        description: Agrupamento cadastrado com sucesso
    """
    data = request.get_json()
    novo_agrupamento = Agrupamento(
        id=data['id'],
        quantidade_de_toras=data['quantidade_de_toras'],
        peso=data['peso']
    )
    db.session.add(novo_agrupamento)
    db.session.commit()
    return jsonify({"message": "Agrupamento cadastrado com sucesso!"}), 200


@app.route('/buscar_agrupamentos', methods=['GET'])
def buscar_agrupamentos():
    """
    Listar todos os agrupamentos
    ---
    tags:
      - Agrupamentos
    responses:
      200:
        description: Lista de agrupamentos
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              quantidade_de_toras:
                type: integer
                example: 10
              peso:
                type: number
                format: float
                example: 1200.5
    """
    agrupamentos = Agrupamento.query.all()
    return jsonify([
        {"id": agrupamento.id, "quantidade_de_toras": agrupamento.quantidade_de_toras, "peso": agrupamento.peso}
        for agrupamento in agrupamentos
    ]), 200


@app.route('/deletar_agrupamento/<int:id>', methods=['DELETE'])
def deletar_agrupamento(id):
    """
    Deletar um agrupamento pelo ID
    ---
    tags:
      - Agrupamentos
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: ID do agrupamento a ser deletado
    responses:
      200:
        description: Agrupamento deletado com sucesso
    """
    agrupamento = Agrupamento.query.get_or_404(id)
    db.session.delete(agrupamento)
    db.session.commit()
    return jsonify({"message": "Agrupamento deletado com sucesso!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
