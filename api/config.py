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


class Config:

    # Configura SECRET_KEY
    SECRET_KEY = getenv('SECRET_KEY', gera_chave_secreta())

    # Configura URL do banco de dados.
    # Em caso de erro, a aplicação usa um banco de dados local sqlite3
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')\
        or 'sqlite:///application.db'

    # Desativa o rastreamento de modificações
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configura REDIS para caching
    REDIS_URL = getenv('REDIS_URL')
