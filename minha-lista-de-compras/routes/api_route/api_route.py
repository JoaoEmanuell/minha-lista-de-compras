from flask import Blueprint, jsonify

from .routes_class import hash_sub_route

api = Blueprint('api', __name__)

# Sub routes

api.register_blueprint(hash_sub_route, url_prefix='/hash')

@api.route('/')
def api_index():
    return jsonify({'Hello': 'World'})