from os import environ as env

from dotenv import load_dotenv

from .mongo_database import MongoDatabase

load_dotenv()

mongo = MongoDatabase(
    database_name='minha-lista-de-compras',
    host=env['MONGO_HOST'],
    port=int(env['MONGO_PORT']),
    username=env['MONGO_ROOT_USERNAME'],
    password=env['MONGO_ROOT_PASSWORD']
)