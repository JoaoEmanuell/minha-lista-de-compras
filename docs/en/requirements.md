- [Requirements](#requirements)
  - [Env file](#env-file)
  - [Docker](#docker)
  - [Node](#node)
    - [Scripts](#scripts)
  - [Python](#python)

# Requirements

Before you start anything [click here](#env-file) to learn how to
configure **.env**

As this project requires Node version v19.10.0 and Python 3.11.0 installed.

    node==19.10.0
    python==3.11.0

Or if you want to use docker, which is more recommended, in that case install
docker and docker-compose

    docker=>20.10.12
    docker-compose=>1.25.0

If you want to use only docker, [click here](#docker)

If you didn't want to use docker, [click here](#node)

## Env file

The env file is responsible for the environment variables.

Create a file called **.env** in the project root, after that copy the
data from **env_example** to it.

Substitute the values after each **=**

     MONGO_ROOT_USERNAME=mongo root username # Mongo root username
     MONGO_ROOT_PASSWORD=mongo root password # Mongo root password

     MONGO_ROOT_USERNAME=root
     MONGO_ROOT_PASSWORD=example

Also generate an encryption key, just run the **new_fernet_key.py** file
located in **minha-lista-de-compras/utils**, copy the generated key and the
put it inside the key **ENCRYPTION_KEY** in the .env, this process must be done
regardless of whether you run the project using Docker or without it.

## Docker

Build the image

     docker-compose build

This way the environment is already configured.

## Node

This app uses typescript and is packaged with webpack.

Install the necessary libs for operation

    npm install

### Scripts

The **start** scripts performs the compilation of the typescript to javascript through tsc.

The **build** script performs the packaging of the files.

**Tip:** If you want to save time, install **npm-run-all** globally

    npm install npm-run-all -g

After that just run

    npm-run-all start build

To compile the typescript codes and package the files.

## Python

To get stared in python, create the virtual environment

Linux:

    python -m venv .

Windows:

    py -m venv .

After that activate it

Linux:

    source ./bin/activate

Windows:

    \Scripts\activate

Install requirements.txt

    pip install -r requirements.txt

To run the **tests** you must create a symbolic link to the folder
**minha-lista-de-compras**, if it is not created the tests cannot be executed.

Linux:

    ln -s minha-lista-de-compras mlc

Windows:

    mklink minha-lista-de-compras mlc

**Note:**

The entire **tests** path is configured as being in the **tests** folder, so the tests are run as follows:

    pytest path_to_test/test.py

This way the environment is already configured.

[Return](./README.md)