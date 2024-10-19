import secrets
import os
from os import getenv
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()


# Gera uma SECRET_KEY, caso não
# seja fornecida no arquivo .env
def gera_chave_secreta():
    return secrets.token_hex()


def retorna_config_banco_de_dados():

    # Obtendo variáveis de ambiente para banco de dados
    try:
        DB_URL = getenv('DATABASE_URL')

        if DB_URL:
            return DB_URL

        DATABASE_USER = getenv('DATABASE_USER')
        DATABASE_PASSWORD = getenv('DATABASE_PASSWORD')
        DATABASE_HOST = getenv('DATABASE_HOST')
        DATABASE_PORT = getenv('DATABASE_PORT')
        DATABASE_NAME = getenv('DATABASE_NAME')
        DATABASE_TYPE = getenv('DATABASE_TYPE')

        # Criando a string para conexão
        connection_string = f"{DATABASE_TYPE}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

    except:
        # Em caso de erro, retorne None
        pass

    return None


class Config:

    # Configura SECRET_KEY
    SECRET_KEY = getenv('SECRET_KEY', gera_chave_secreta())

    # Configura URL do banco de dados.
    # Em caso de erro, a aplicação usa um banco de dados local sqlite3
    SQLALCHEMY_DATABASE_URI = retorna_config_banco_de_dados()\
        or 'sqlite:///application.db'

    # Desativa o rastreamento de modificações
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configura REDIS para caching
    REDIS_URL = getenv('REDIS_URL')


class TestConfig:
    # Configura SECRET_KEY
    SECRET_KEY = gera_chave_secreta()

    # Configura URL do banco de dados em memória.
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # Desativa o rastreamento de modificações
    SQLALCHEMY_TRACK_MODIFICATIONS = False
