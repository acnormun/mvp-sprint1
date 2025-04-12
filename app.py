from flask import Flask, jsonify, request
from swagger_config import setup_swagger
from flask_cors import CORS

from routes.agrupamento import agrupamento_bp, db as agrupamento_db
from routes.logistic import logistic_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agrupamentos.db'

CORS(app)

agrupamento_db.init_app(app)
setup_swagger(app)

app.register_blueprint(agrupamento_bp)
app.register_blueprint(logistic_bp)

with app.app_context():
    agrupamento_db.create_all()

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')
