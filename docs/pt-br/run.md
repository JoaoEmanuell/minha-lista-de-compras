- [Rodando o projeto](#rodando-o-projeto)
  - [Docker](#docker)
  - [Servidor](#servidor)
  - [Compilado os arquivos estáticos](#compilado-os-arquivos-estáticos)

# Rodando o projeto

Uma vez que tudo foi instalado e configurado corretamente [Leia Requerimentos](./requirements.md) caso não tenha instalado os requerimentos.

## Docker

Digite o comando:

    docker-compose up

Com isso o servidor já estará rodando.

**DICA:**

Caso queira abrir o shell no container, utilize o seguinte comando

    docker exec -it minha-lista-de-compras_web_1 sh

## Servidor

Para iniciar o servidor navegue até a pasta **minha-lista-de-compras**

    cd minha-lista-de-compras

Inicie o servidor utilizando o comando seguinte comando:

    flask run

Caso queria iniciar ele em modo de debug utilize:

    FLASK_DEBUG=true flask run

## Compilado os arquivos estáticos

Como mencionado anteriormente, os arquivos estáticos são os arquivos css e javascript utilizados no front-end.

Dentro da pasta **raiz**, utilize os seguintes comandos:

    npm run start
    
    npm run build

Ou caso tenha instalado o **npm-run-all**

    npm-run-all start build

**Nota:** Caso você esteja utilizado o **tsc --watch** para compilar os arquivos typescript, basta apenas utilizar o **npm run build**

**Nota:** Esse processo deve ser feito a cada nova alteração nos arquivos estáticos.

[Retornar](./README.md)