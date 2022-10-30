from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)

@api.route('/')
def api_index():
    return jsonify({'Hello': 'World'})