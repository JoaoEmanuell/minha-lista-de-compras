from os import environ as env

from requests import get, post
from dotenv import load_dotenv

load_dotenv(
    dotenv_path='./.env/'
)


def test_answer():
    api_url = "http://127.0.0.1:8080/api"
    API_TOKEN = env["API_TOKEN"]
    ENCRYPTION_KEY = env["ENCRYPTION_KEY"]

    # Index

    response = get(api_url).json()
    assert type(response) == dict
    assert response["Hello"] == "World"

    # Hash

    ## Generate

    new_hash_url = f"{api_url}/hash/new_hash"

    ### Valid

    data = {"text": "Hello World"}
    response = post(url=new_hash_url, json=data).json()
    assert type(response) == dict
    assert response["hash"][0:10] == "a591a6d40b"
    full_hash = response["hash"]

    ### Invalid
    invalid_data = {"hash": "Hello World"}
    response = post(url=new_hash_url, json=invalid_data).json()
    assert response["hash"] == "Invalid Key"

    ## Compare

    compare_hash_url = f"{api_url}/hash/compare_hash"

    ### Valid
    data["hash"] = full_hash
    response = post(url=compare_hash_url, json=data).json()
    assert type(response) == dict
    assert response["equal"] == True

    ### Invalid
    response = post(url=compare_hash_url, json=invalid_data).json()
    assert response["equal"] == "Invalid Key"

    # Encrypt

    ## Valid

    encrypt_url = f"{api_url}/encrypt"
    data = {
        "token": API_TOKEN,
        "key": ENCRYPTION_KEY,
        "data": ["test", "text", "text2"],
    }
    encrypt_valid_response = post(url=f"{encrypt_url}/encrypt", json=data).json()
    assert type(encrypt_valid_response) == dict
    assert type(encrypt_valid_response["encrypted_data"]) == list
    assert len(encrypt_valid_response["encrypted_data"]) == 3

    ## Invalid

    ### Token
    data["token"] = "foo"
    response = post(url=f"{encrypt_url}/encrypt", json=data).json()
    assert response == {"error": "Invalid token"}

    ### Key
    data["token"] = API_TOKEN
    data["key"] = "foo"
    response = post(url=f"{encrypt_url}/encrypt", json=data).json()
    assert response == {"error": "Invalid Encrypt Key"}

    # Decrypt

    ## Valid

    data = {
        "token": API_TOKEN,
        "key": ENCRYPTION_KEY,
        "data": encrypt_valid_response["encrypted_data"],
    }
    response = post(url=f"{encrypt_url}/decrypt", json=data).json()
    assert type(response) == dict
    assert len(response["decrypted_data"]) == 3
    assert response["decrypted_data"] == ["test", "text", "text2"]

    ## Invalid

    ### Token
    data["token"] = "foo"
    response = post(url=f"{encrypt_url}/decrypt", json=data).json()
    assert response == {"error": "Invalid token"}

    ### Key
    data["token"] = API_TOKEN
    data["key"] = "foo"
    response = post(url=f"{encrypt_url}/decrypt", json=data).json()
    assert response == {"error": "Invalid Encrypt Key"}
