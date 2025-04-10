# **API de Agrupamentos de Madeira**

Este projeto é uma API em Flask para gerenciar **agrupamentos de madeira**, permitindo o cadastro, listagem, edição, exclusão e cálculo de frete com base em dois CEPs. Utiliza a API externa **ViaCEP** e **Geoapify** para geolocalização e cálculo de distância. Toda a documentação está disponível via Swagger.

---

## **Requisitos**

- Python 3.10+
- Docker (para execução com container)

---

## **Instalação com Docker**

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/mvp-api.git
cd mvp-api
```

2. Construa a imagem Docker:
```bash
docker build -t mvp-api .
```

3. Rode o container:
```bash
docker run -p 5000:5000 mvp-api
```

---

## **Rotas da API**

### **Base URL**
- `http://localhost:5000`

### **Documentação Swagger**
- Acesse [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

### **Endpoints**

#### **1. Cadastrar Agrupamento**
- `POST /cadastrar_agrupamento`

#### **2. Buscar Agrupamentos**
- `GET /buscar_agrupamentos`

#### **3. Editar Agrupamento**
- `PUT /editar_agrupamento/<id>`

#### **4. Deletar Agrupamento**
- `DELETE /deletar_agrupamento/<id>`

#### **5. Calcular Frete**
- `POST /calcular_frete`
- Corpo:
```json
{
  "cep_origem": "30130-010",
  "cep_destino": "01310-000"
}
```
- Retorna distância em km e cálculo estimado do frete com base no peso informado.

---

## **Tecnologias Utilizadas**

- Flask
- Flask-SQLAlchemy
- Flasgger
- Flask-CORS
- Requests
- SQLite

---

## **API Externa Utilizada**

- **ViaCEP**: [https://viacep.com.br](https://viacep.com.br)
- **Geoapify**: [https://www.geoapify.com/](https://www.geoapify.com/)
  - Gratuita (até 3.000 requisições por dia)
  - Requer criação de chave (API Key)

---

## **Personalização**

- O banco de dados está em `agrupamentos.db`
- A documentação está em `swagger_config.py`

---

## **Licença**

Este projeto está sob a licença MIT.

---

Feito por ACNormun 🐝
