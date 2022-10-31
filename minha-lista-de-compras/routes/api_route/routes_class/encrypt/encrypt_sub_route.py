from os import environ as env

from flask import Blueprint
from dotenv import load_dotenv

from .source import Encrypt

load_dotenv()

ENCRYPTION_KEY = env['ENCRYPTION_KEY']

encrypt = Encrypt(ENCRYPTION_KEY)

encrypt_sub_route = Blueprint('encrypt', __name__)

@encrypt_sub_route.route('/encrypt')
def encrypt_route():
    return 'encrypt_route'

@encrypt_sub_route.route('/decrypt')
def decrypt_route():
    return 'decrypt_route'