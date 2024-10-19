# 🐍 FLASK-END API 🌶️

Esta é uma API Back End desenvolvida em Flask, utilizando Flask-RESTful e Flask-SQLAlchemy.

Toda a comunicação da API acontece em formato JSON.

A API contém todas as funções propostas conforme o Back End Challenge, incluindo:

* Documentação completa

* Script para Deploy com Docker

* Script para automação YML, para garantir desenvolvimento e integração contínuos (CI/CD).

* Possui funcionalidade de integração com PostgreSQL por padrão. Com a utilização de variáveis de ambiente.



# Demonstração - Live Demo 🤖🔥

A API está disponível publicamente e pode ser acessada através do link abaixo.

Ela está em execução utilizando PostgreSQL para armazenamento em banco de dados.

Link para a demonstração: [FlaskEnd API - Live Demo](https://flaskend-production.up.railway.app/users/)



## Estrutura e Endpoints:

| Método | Endpoint | Descrição | 
| ------ | -------- | -
| GET    | `/users` | Lista todos os cadastros
| GET    | `/users/<int:id>` | Consulta um usuário pelo id
| POST   | `/users` | Cria um novo usuário
| DELETE | `/users/<int:id>` | Deleta um usuário


### 1. GET /users/
Retorna todos os usuários cadastrados e seus papéis.

**Exemplo de Resposta:**
```json
[
    {
        "id": 1,
        "name": "Bob Kerman",
        "email": "bob@example.com",
        "role_description": "Manager",
        "claim_description": "Edit Reports"
    },
    {
        "id": 2,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "role_description": "Admin",
        "claim_description": "Delete Reports"
    }
]
```


### 2. GET /users/\<int:user_id\>
Retorna o papel de um usuário específico de acordo com seu user_id.

**Exemplo de Requisição:**

```python
GET http://localhost:5000/users/3
```

**Exemplo de Resposta:**
```json
{
    "user_id": 3,
    "name": "Vall Kerman",
    "role_description": "User",
    "role_id": 3
}
```


### 3. POST /users
Cria um novo usuário. Se nenhuma senha for fornecida, uma senha será gerada automaticamente.

**Exemplo de Requisição:**
```json
{
    "username": "Bill Edward",
    "role": "User",
    "email": "bill@example.com"
}
```

**Exemplo de Resposta:**
```json
{
	"message": "Usuario cadastrado com sucesso"
}
```


### 4. DELETE /users/\<int:user_id\>
Deleta um usuário específico de acordo com seu user_id.

**Exemplo de Requisição:**

```python
DELETE http://localhost:5000/users/3
```

**Exemplo de Resposta:**
```json
{
	"message": "Usuario removido"
}
```




# Instruções para instalação 🔧

## Execução Local 💻

Para executar a aplicação localmente, siga os passos abaixo.

Pré-requisitos:
* Python 3.11 ou superior
* Pip (gerenciador de pacotes do Python)
* Virtualenv (opcional, mas recomendado)


    ## 1. Crie um ambiente virtual (opcional):

    ```bash
    python3.11 -m venv venv

    # No Linux ou MacOS
    source venv/bin/activate 

    # No Windows use:
    venv\Scripts\activate
    ```

    ## 2. Navegue para a pasta do projeto

    ```bash
    cd src
    ```

    ## 3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

    ## 4. Configure as variáveis de ambiente (opcional):

    Crie um arquivo .env na raiz do projeto (pasta onde o arquivo ".env.example" se encontra) e adicione suas configurações, como a URL do banco de dados.

    ## 5. Execute a aplicação:

    ```bash
    flask --app app run --debug
    ```

    A aplicação estará disponível em http://localhost:5000.



# Deploy com Docker 🐋

Para realizar o deploy da aplicação utilizando Docker, siga os passos abaixo:


## 1. Navegue para a pasta do projeto

```bash
cd src
```

## 2. Crie uma imagem Docker:

```bash
docker build -t flaskend .
```

Execute o container:

```bash
docker run -p 5000:5000 flaskend
```

A aplicação estará acessível através do endereço IP do seu contêiner Docker, na porta 5000. Você pode acessá-la utilizando o seguinte link:

http://localhost:5000 ou http://\<ip-do-seu-docker\>:5000



# Testes com UnitTest 🐍🔥

Este projeto inclui uma suíte de testes automatizados para garantir a funcionalidade da API. Os testes estão localizados no arquivo `tests/test_api.py`.

## Executando os Testes

Para executar os testes da API, utilize o seguinte comando no terminal:

```bash
python -m unittest tests/test_api.py
```

## O que o teste avalia:

Os testes foram projetados para verificar as principais funções da API, incluindo:

* Verifica se a lista de usuários é retornada corretamente.

* Confirma que um usuário específico pode ser recuperado com base no ID.
    
* Testa a criação e a remoção de um novo usuário.


## Por que Testar?

A execução regular dos testes ajuda a identificar rapidamente qualquer problema na funcionalidade principal da API, garantindo que as alterações no código não introduzam novos erros ou bugs.



# CI/CD com GitHub Actions 🐧 (Opcional)

Ao realizar um push na branch main, o código atualizado será enviado para deploy em um container. Para configurar o CI/CD, configure o arquivo de workflow em .github/workflows e/ou Dockerfile na raiz do projeto.


# Caching com Redis 📦 (Opcional)

Para melhorar a performance da aplicação, você pode integrar o Redis como um sistema de cache. Para isso, siga os passos abaixo:

## 1. Edite o arquivo ".env"

Use seu editor de texto favorito para editar o endereço do seu banco de dados Redis.

Edite o arquivo ".env":

```bash
REDIS_URL=http://<seu-endereço-redis.com>:80/
```

## 2. Instale as dependências

```python
pip install flask-redis
```

## 2. Atualize as rotas da API

Edite `app.py` para incluir as rotas que devem ficar em cache, conforme a documentação

```python
from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)

redis_client = FlaskRedis(app)

@app.route('/')
def index():
    return redis_client.get('Hello_World')
```

Para consultar a documentação completa, visite: [Flask-Redis](https://pypi.org/project/flask-redis/)


# Referências e Links: 📚

Documentação [Flask Framework](https://flask.palletsprojects.com/en/3.0.x/)

Documentação [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/)


Documentação [Flask RESTful](https://flask-restful.readthedocs.io/en/latest/)

Documentação [Flask Seeders](https://pypi.org/project/Flask-Seeder/)


Artigo sobre [Design Patterns (Adapter)](https://refactoring.guru/pt-br/design-patterns/adapter)


