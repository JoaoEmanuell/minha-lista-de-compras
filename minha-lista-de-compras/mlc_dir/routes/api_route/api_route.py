from flask import Blueprint, jsonify

from .routes_class import hash_sub_route, encrypt_sub_route

api = Blueprint("api", __name__)

# Sub routes

api.register_blueprint(hash_sub_route, url_prefix="/hash")
api.register_blueprint(encrypt_sub_route, url_prefix="/encrypt")


@api.route("/")
def api_index():
    print('Index api route')
    return jsonify({"Hello": "World"})
