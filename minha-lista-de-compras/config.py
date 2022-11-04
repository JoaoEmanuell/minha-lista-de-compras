from os import environ as env
from os.path import join
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

absolute_path = Path().absolute()

# Sqlalchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(absolute_path, 'database.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# CSRF

SECRET_KEY=env['SECRET_KEY_CSRF']

# Mongo

MONGO_ROOT_USERNAME=env['MONGO_ROOT_USERNAME']
MONGO_ROOT_PASSWORD=env['MONGO_ROOT_PASSWORD']
MONGO_HOST=env['MONGO_HOST']
MONGO_PORT=env['MONGO_PORT']