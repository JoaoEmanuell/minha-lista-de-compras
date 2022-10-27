- [Running the project](#running-the-project)
  - [Docker](#docker)
  - [Server](#server)
  - [Compiled the static files](#compiled-the-static-files)

# Running the project

Once everything has been installed and configured correctly [Read Requirements](./requirements.md) if you haven't installed the requirements.

## Docker

Write the command:

    docker-compose up

With that the server will be running.

**TIP:**

If you want to open the shell in the container, use the following command

    docker exec -it minha-lista-de-compras_web_1 sh

## Server

To start the server navigate to the **my-shopping-list** folder

    my-shopping-list cd

Start the server using the following command:

    flask run

If you want to start it in debug mode use:

    FLASK_DEBUG=true flask run

## Compiled the static files

As mentioned earlier, static files are the css and javascript files used in the front end.

Inside the **root** folder, use the following commands:

    npm run start
    
    npm run build

Or if you have installed **npm-run-all**

    npm-run-all start build

**Note:** If you are using **tsc --watch** to compile the typescript files, just use **npm run build**

**Note:** This process must be done with each new change to static files.

[Return](./README.md)