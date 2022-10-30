from requests import get

def test_answer():
    api_url = 'http://127.0.0.1:8080/api'
    
    # Index

    response = get(api_url).json()
    assert type(response) == dict
    assert response['Hello'] == 'World'