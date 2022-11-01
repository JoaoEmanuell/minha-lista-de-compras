from os import environ as env

from flask import Blueprint, jsonify, request
from dotenv import load_dotenv

from source import Factory, EncryptInterface

load_dotenv()

fac = Factory()

API_TOKEN = env['API_TOKEN']

Encrypt = fac.get_representative(EncryptInterface) # Class

encrypt_sub_route = Blueprint('encrypt', __name__)

@encrypt_sub_route.route('/encrypt', methods=['POST'])
def encrypt_route():
    if request.method == 'POST':
        keys = ('token', 'key', 'data', )
        data: dict = request.json

        for key in keys:
            if key not in data:
                return jsonify({'error': f'Invalid key {key}'})

        if data['token'] != API_TOKEN:
            return jsonify({'error': 'Invalid token'})
        
        try:
            encrypt: EncryptInterface = Encrypt(data['key'])
        except Exception:
            return jsonify({'error': 'Invalid Encrypt Key'})
        else:
            encrypt_data = encrypt.encrypt(data['data'])
            return jsonify({'encrypted_data': encrypt_data})

@encrypt_sub_route.route('/decrypt', methods=['POST'])
def decrypt_route():
    if request.method == 'POST':
        keys = ('token', 'key', 'data', )
        data: dict = request.json

        for key in keys:
            if key not in data:
                return jsonify({'error': f'Invalid key {key}'})

        if data['token'] != API_TOKEN:
            return jsonify({'error': 'Invalid token'})
        
        try:
            encrypt: EncryptInterface = Encrypt(data['key'])
        except Exception:
            return jsonify({'error': 'Invalid Encrypt Key'})
        else:
            decrypted_data = encrypt.decrypt(data['data'])
            return jsonify({'decrypted_data': decrypted_data})