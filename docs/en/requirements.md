- [Requirements](#requirements)
  - [Node](#node)
    - [Scripts](#scripts)
  - [Python](#python)

# Requirements

As this project requires Node version v15.14.0 or higher and Python 3.10.7 higher installed.

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