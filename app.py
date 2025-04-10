from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from swagger_config import setup_swagger

# Importa os blueprints e o db
from routes.agrupamento import agrupamento_bp, db as agrupamento_db
from routes.logistic import logistic_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agrupamentos.db'
CORS(app)

# Inicializa o banco com a app
agrupamento_db.init_app(app)

# Configuração do Swagger
setup_swagger(app)

# Registra os blueprints
app.register_blueprint(agrupamento_bp)
app.register_blueprint(logistic_bp)

# Cria as tabelas no banco de dados
with app.app_context():
    agrupamento_db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
