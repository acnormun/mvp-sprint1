
# **API de Agrupamentos de Madeira**

Este projeto é uma API simples para gerenciar **agrupamentos de madeira**, permitindo o cadastro, listagem e exclusão de agrupamentos. Ele utiliza **Flask**, **Flask-SQLAlchemy** para gerenciamento do banco de dados SQLite, e **Flasgger** para documentação automática das rotas com Swagger.

---

## **Requisitos**

- Python 3.7+
- Pip (gerenciador de pacotes Python)

---

## **Instalação**

1. Clone este repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd mvp-agrupamentos
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install flask flask-sqlalchemy flasgger
   ```

4. Execute a aplicação:
   ```bash
   python app.py
   ```

---

## **Rotas da API**

### **Base URL**
- `http://localhost:5000`

### **Documentação Swagger**
- Acesse [http://localhost:5000/apidocs](http://localhost:5000/apidocs) para visualizar e testar as rotas da API.

### **Endpoints**

#### **1. Cadastrar Agrupamento**
- **Rota**: `POST /cadastrar_agrupamento`
- **Descrição**: Cadastra um novo agrupamento de madeira.
- **Corpo da Requisição**:
  ```json
  {
    "quantidade_de_toras": 10,
    "peso": 1200.5
  }
  ```
- **Resposta**:
  ```json
  {
    "message": "Agrupamento cadastrado com sucesso!"
  }
  ```

#### **2. Buscar Agrupamentos**
- **Rota**: `GET /buscar_agrupamentos`
- **Descrição**: Retorna todos os agrupamentos cadastrados.
- **Resposta**:
  ```json
  [
    {
      "id": 1,
      "quantidade_de_toras": 10,
      "peso": 1200.5
    }
  ]
  ```

#### **3. Deletar Agrupamento**
- **Rota**: `DELETE /deletar_agrupamento/<id>`
- **Descrição**: Deleta um agrupamento pelo seu `id`.
- **Parâmetro**:
  - `id`: ID do agrupamento a ser deletado.
- **Resposta**:
  ```json
  {
    "message": "Agrupamento deletado com sucesso!"
  }
  ```

---

## **Tecnologias Utilizadas**

- **Flask**: Framework web.
- **Flask-SQLAlchemy**: ORM para gerenciar o banco de dados SQLite.
- **Flasgger**: Geração automática de documentação Swagger.

---

## **Como Personalizar**

- **Banco de Dados**: A configuração do banco de dados está em `app.config['SQLALCHEMY_DATABASE_URI']`. Por padrão, utiliza um arquivo SQLite chamado `agrupamentos.db`.
- **Documentação Swagger**: A documentação está configurada no arquivo `swagger_config.py`.

---

## **Próximos Passos**

- Adicionar autenticação (opcional).
- Melhorar validação dos dados de entrada com `marshmallow` ou `pydantic`.
- Deploy em um servidor (Heroku, AWS, etc.).

---

## **Contribuição**

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## **Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

Feito por ACNormun 🐝
