from flask import Flask
from flask_restful import Api

# Importa configurações para aplicação
from api.config import Config

# Importa módulos da API
from api.database import db
from api.models import Roles
from api.routes import UsersResource

# Importa seed para banco inicial
from api.seeder import RolesAndClaimsSeeder


# Cria App Flask
app = Flask(__name__)
api = Api(app)

# Configura App Flask
app.config.from_object(Config)


# Inicia extensão do SQLAlchemy
db.init_app(app)

with app.app_context():
    # Cria tabelas no banco de dados
    db.create_all()

    # Verifica se não há roles no
    # banco de dados
    #
    if not Roles.query.first():
        # Executa o seeder
        # Caso o banco esteja vazio,
        # esse comando cria Roles e
        # Claims para propositos de
        # teste

        seeder = RolesAndClaimsSeeder()
        seeder.run()


# Define URL Base para o endpoint
# BASE_URL = "/api/v1"

# Registra rota
# api.add_resource(UsersResource, f"{BASE_URL}/", f"{BASE_URL}/users/<int:user_id>")


# Registra rota
api.add_resource(UsersResource, "/users/", "/users/<int:user_id>")


if __name__ == '__main__':
    app.run()
