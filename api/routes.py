from flask import request, jsonify
from flask_restful import Resource

from api.database import db
from api.models import Users, Roles, Claims, UserClaims

from api.utils import consulta_com_join
from api.utils import cria_usuario_no_banco
from api.utils import consulta_dados_de_usuario
from api.utils import deleta_usuario_por_id


class UsersResource(Resource):
    #
    # GET /users/
    #
    # GET /users/<int:user_id>
    #
    def get(self, user_id=None):
        if user_id is None:
            # Retorna consulta com todos os usuarios
            return consulta_com_join()

        # Retorna consulta de um usuário específico
        return consulta_dados_de_usuario(user_id)

    #
    # Endpoint:
    # POST /users
    #
    # Resposável por criar usuários
    #
    def post(self):
        '''
        4.- Utilizando a mesma estrutura do banco de dados fornecida
        anteriormente, e a linguagem que desejar, construa uma
        API REST que irá criar um usuário. Os campos obrigatórios
        serão nome, e-mail e papel do usuário.
        A senha será um campo opcional, caso o usuário não informe
        uma senha o serviço da API deverá gerar essa senha automaticamente.
        '''

        return cria_usuario_no_banco(request)

    def delete(self, user_id=None):
        '''
            Deleta um usuário, de acordo
            com o user_id
        '''
        if user_id is None:
            return {'message': 'id inválido'}

        return deleta_usuario_por_id(user_id)
