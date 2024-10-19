from flask import request, jsonify

import secrets
from werkzeug.security import generate_password_hash

from api.database import db

from api.models import Users, Roles
from api.models import Claims, UserClaims


def consulta_com_join():

    # Query SQL usando ORM do Flask SQLAlchemy
    resultado_da_query = db.session.query(Users, Roles, Claims).\
        join(Roles, Users.role_id == Roles.id).\
        outerjoin(UserClaims, Users.id == UserClaims.user_id).\
        outerjoin(Claims, UserClaims.claim_id == Claims.id).\
        all()

    # Variável que vai ser retornada
    retorno_da_consulta = []

    for user, role, claim in resultado_da_query:
        retorno_da_consulta.append({
            "name": user.name,
            "email": user.email,
            "role_description": role.description if role else None,
            "claim_description": claim.description if claim else None,
        })

    # Retorna consulta no formato JSON
    return jsonify(retorno_da_consulta)


def consulta_dados_de_usuario(user_id: int):

    # Query SQL usando ORM do Flask SQLAlchemy
    resultado_da_query = db.session.query(Users, Roles).\
        filter(Users.id == user_id).\
        join(Roles, Users.role_id == Roles.id).all()

    if not resultado_da_query:
        # Caso usuário não exista, retorna um erro
        return jsonify({'message': 'Usuário não encontrado'})

    # Variável que vai ser retornada
    retorno_da_consulta = []

    for user, role in resultado_da_query:
        retorno_da_consulta.append({
            "user_id": user_id,
            "name": user.name,
            "role_id": role.id,
            "role_description": role.description,
        })

    return jsonify(retorno_da_consulta)


# Função auxiliar que gera senha aleatória
def gera_senha():
    '''
        Retorna uma senha aleatória
    '''
    return secrets.token_hex(8)


def verifica_se_email_tem_cadastro(email_do_usuario):
    '''
        Retorna o endereço de email cadastrado caso
        ele exista, ou retorna None caso o email não exista.
    '''
    email = Users.query.filter_by(email=email_do_usuario).first()

    return email


def cria_usuario_no_banco(request):

    try:
        username = request.json['username']
        password = request.json.get('password', gera_senha())
        role = request.json['role']
        email = request.json['email']

    except KeyError as e:
        return {'message': f"Missing {e} field."}

    #
    # Antes que o cadastro seja realizado,
    # confira se email de usuario já está em uso.
    #
    if verifica_se_email_tem_cadastro(email):
        return {'message': 'Email ja possui cadastro'}

    #
    # Confere se o Role Existe
    #
    consulta_role_id_por_nome = Roles.query.filter_by(description=role).first()

    # Retorna mensagem caso Role não exista
    if not consulta_role_id_por_nome:
        return {'message': 'Invalid Role'}, 404

    #
    # Cria instância da classe User
    #
    novo_usuario = Users(
        name=username,
        email=email,
        password=password
    )

    # Adiciona novo_usuario a sessão SQLAlchemy
    db.session.add(novo_usuario)

    # Configura Role para novo_usuario
    novo_role_id = consulta_role_id_por_nome.id

    # Configura novo_usuário com Role_id
    novo_usuario.role_id = novo_role_id

    # Consulta permissão padrão
    consulta_claim = Claims.query.first()

    # Adiciona uma permissão inicial
    # na tabela User_Claims
    nova_claim = UserClaims(
        user_id=novo_usuario.id,
        claim_id=consulta_claim.id
    )

    # Adiciona informações para serem salvas
    # na instância do SQLAlchemy (variável db)
    db.session.add(nova_claim)

    # Salva todas as alterações no banco de dados.
    # Incluindo Users, Roles, Claims e UserClaims
    db.session.commit()

    return {'message': 'Usuario cadastrado com sucesso'}


def deleta_usuario_por_id(user_id: int):

    # Query SQL usando ORM do Flask SQLAlchemy
    resultado_da_query = db.session.query(Users).\
        filter(Users.id == user_id).\
        first()

    if not resultado_da_query:
        # Caso usuário não exista, retorna um erro
        return jsonify({'message': 'Usuário não encontrado'})

    # Remove Usuario
    db.session.delete(resultado_da_query)
    db.session.commit()

    return jsonify({'message': 'Usuario removido'})
