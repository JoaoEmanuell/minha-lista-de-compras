from os import environ as env
from json import dump

from requests import get, post

def test_answer():
    api_url = 'http://127.0.0.1:8080/api'
    
    # Index

    response = get(api_url).json()
    assert type(response) == dict
    assert response['Hello'] == 'World'

    # Hash

    ## Generate

    new_hash_url = f'{api_url}/hash/new_hash'

    ### Valid

    data = {'text': 'Hello World'}
    response = post(
        url=new_hash_url,
        json=data
    ).json()
    assert type(response) == dict
    assert response['hash'][0:10] == 'a591a6d40b'
    full_hash = response['hash']

    ### Invalid
    invalid_data = {'hash': 'Hello World'}
    response = post(
        url=new_hash_url,
        json=invalid_data
    ).json()
    assert response['hash'] == 'Invalid Key'

    ## Compare

    compare_hash_url = f'{api_url}/hash/compare_hash'

    ### Valid
    data['hash'] = full_hash
    response = post(
        url=compare_hash_url,
        json=data
    ).json()
    assert type(response) == dict
    assert response['equal'] == True

    ### Invalid
    response = post(
        url=compare_hash_url,
        json=invalid_data
    ).json()
    assert response['equal'] == 'Invalid Key'

    # Encrypt

    ENCRYPTION_KEY = env['ENCRYPTION_KEY']

    encrypt_url = f'{api_url}/encrypt'
    data = {
        'key': ENCRYPTION_KEY,
        'data': ['test', 'text', 'text2']
    }
    response = post(
        url=f'{encrypt_url}/encrypt', 
        json=data
    ).json()
    assert type(response) == dict
    assert type(response['encrypted_data']) == list
    assert len(response['encrypted_data']) == 3

    '''response = post(f'{encrypt_url}/decrypt').json()
    assert response == {'route': 'decrypt_route'}'''