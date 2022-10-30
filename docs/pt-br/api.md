- [Api](#api)
- [Rotas](#rotas)
  - [Hash](#hash)
    - [New hash](#new-hash)
    - [Compare hash](#compare-hash)
  - [Encrypt](#encrypt)
    - [Encrypt](#encrypt-1)
    - [Decrypt](#decrypt)

# Api

A api é usada para controle geral do site, interação com o banco de dados, criptografia, geração de hash e etc.

# Rotas

Nome: **Nome da rota**

Tipo: **GET** or **POST**

Descrição:

    Descrição da rota

Parâmetros:

    Parâmetros da rota

Retorno:

    Exemplo do json de retorno

****

## Hash

Sub-rota responsável pelo gerenciamento de hash

****

### New hash

Nome: **new_hash**

Tipo: **POST**

Descrição:

    Gera um novo hash baseado no texto passado para ela.

Parâmetros:

    {
        'text': 'Texto que será transformado em hash'
    }

Retorno:

    {
        'hash': 'Hash gerado pelo texto' # str
    }

### Compare hash

Nome: **compare_hash**

Tipo: **POST**

Descrição:

    Compara hash gerados pela new_hash

Parâmetros:

    {
        'text': 'Texto base, usado para gerar o hash',
        'hash': 'Hash para ser comparado'
    }

Retorno:

    {
        'equal': true # bool
    }

****

## Encrypt

Sub-rota responsável pelos processos de criptografia.

****

### Encrypt

Nome: **encrypt**

Tipo: **POST**

Descrição:

    Criptografa os dados passados para ela

Parâmetros:

    {
        'key': 'chave de criptografia, gerada pelo servidor',
        'data': ['Dados para criptografar']
    }

Retorno:

    {
        'encrypted_data': ['Dados criptografados']
    }

### Decrypt

Nome: **decrypt**

Tipo: **POST**

Descrição:

    Descriptografa os dados passados para ela

Parâmetros:

    {
        'key': 'chave de criptografia, gerada pelo servidor',
        'data': ['Dados criptografados']
    }

Retorno:

    {
        'decrypt_data': ['Dados criptografados']
    }