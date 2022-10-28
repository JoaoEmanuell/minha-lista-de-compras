from os import environ as env

from dotenv import load_dotenv

from .mongo_database import MongoDatabase

load_dotenv()

mongo = MongoDatabase(
    database_name='minha-lista-de-compras',
    host='127.0.0.1',
    port=27017,
    username=env['MONGO_ROOT_USERNAME'],
    password=env['MONGO_ROOT_PASSWORD']
)