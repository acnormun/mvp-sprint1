from flasgger import Swagger

def setup_swagger(app):
    template = {
        "swagger": "2.0",
        "info": {
            "title": "API de Agrupamentos de Madeira",
            "description": "API para gerenciar agrupamentos de madeira, com funcionalidades de cadastro, listagem e exclusão.",
            "version": "1.0.0"
        },
        "host": "localhost:5000",
        "schemes": ["http"],
    }
    Swagger(app, template=template)
