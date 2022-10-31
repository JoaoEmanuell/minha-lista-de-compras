from flask import Blueprint, jsonify, request

hash_sub_route = Blueprint('hash', __name__)

from .hash_class import Hash

@hash_sub_route.route('/new_hash', methods=['POST'])
def new_hash():
    if request.method == 'POST':
        try:
            data = {
                'text': request.form.get('text', type=str)
            }
            value = Hash().generate_hash(data['text'])
            return jsonify({'hash': value})
        except KeyError:
            return jsonify({'hash' : 'Invalid Key'})
        except TypeError:
            return jsonify({'hash' : 'Invalid JSON'})

@hash_sub_route.route('/compare_hash', methods=['POST'])
def compare_hash():
    if request.method == 'POST':
        try:
            data = {
                'text': request.form.get('text', type=str),
                'hash': request.form.get('hash', type=str)
            }
            compare = Hash().compare_hash(data['text'], data['hash'])
            return jsonify({'equal': compare})
        except KeyError:
            return jsonify({'hash' : 'Invalid Key'})
        except TypeError:
            return jsonify({'hash' : 'Invalid JSON'})