- [Requerimentos](#requerimentos)
  - [Arquivo env](#arquivo-env)
  - [Docker](#docker)
  - [Node](#node)
    - [Scripts](#scripts)
  - [Python](#python)

# Requerimentos

Antes de começar qualquer coisa [clique aqui](#arquivo-env) para aprender a 
configurar o **.env**

Como esse projeto requer o Node versão v19.10.0 e o Python 3.11.0 instalado.

    node==19.10.0
    python==3.11.0

Ou caso queira utilizar o docker, o que é mais recomendado, nesse caso instale 
o docker e o docker-compose

    docker=>20.10.12
    docker-compose=>1.25.0

Caso queira utilizar apenas o docker, [clique aqui](#docker)

Caso não queria utilizar o docker, [clique aqui](#node)

## Arquivo env

O arquivo env é responsável pelas variáveis de ambiente.

Crie um arquivo chamado de **.env** na raiz do projeto, após isso copie os 
dados de **env_example** para ele.

Substitua os valores após cada **=**

    MONGO_ROOT_USERNAME=mongo root username # Mongo root username
    MONGO_ROOT_PASSWORD=mongo root password # Mongo root password

    MONGO_ROOT_USERNAME=root
    MONGO_ROOT_PASSWORD=example

Gere também uma chave de criptografia, só rodar o arquivo **new_fernet_key.py**
localizado em **minha-lista-de-compras/utils**, copie a chave gerada e a 
coloque dentro da key **ENCRYPTION_KEY** no .env, esse processo deve ser feito 
independentemente de você rodar o projeto usando o Docker ou sem ele.

## Docker

Faça a build da imagem

    docker-compose build

Dessa forma o ambiente já está configurado.

## Node

Esse app utiliza o typescript e é empacotado com o webpack.

Instale as libs necessárias para o funcionamento

    npm install

### Scripts

O script **start** executa a compilação do typescript para javascript por meio do tsc.

O script **build** executa o empacotamento dos arquivos.

**Dica:** Caso queira poupar tempo, instale o **npm-run-all** de forma global

    npm install npm-run-all -g

Após isso basta rodar

    npm-run-all start build

Para compilar os códigos typescript e empacotar os arquivos.

## Python

Para começar no python, crie o ambiente virtual

Linux:

    python -m venv .

Windows:

    py -m venv .

Após isso ative ele

Linux:

    source ./bin/activate

Windows:

    \Scripts\activate

Instale o requirements.txt

    pip install -r requirements.txt

Para executar os **tests** você deve criar um link simbólico para a pasta 
**minha-lista-de-compras**, caso não seja criado os testes não poderão ser executados.

Linux:

    ln -s minha-lista-de-compras mlc

Windows:

    mklink minha-lista-de-compras mlc

**Nota:**

Todo o caminho dos **tests** é configurado como estando na pasta **tests**, dessa forma os tests são executados da seguinte maneira:

    pytest path_to_test/test.py

Dessa forma o ambiente já está configurado.

[Retornar](./README.md)