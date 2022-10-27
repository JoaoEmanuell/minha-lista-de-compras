#!/bin/sh

path_to_bin='/usr/local/bin'
pip="${path_to_bin}/pip"
npm="${path_to_bin}/npm"

# Python

$pip install -r requirements.txt

## Pytest

ln -s minha-lista-de-compras mlc

# Node

$npm install
$npm run start
$npm run build

cd minha-lista-de-compras

FLASK_DEBUG=true flask run --host 0.0.0.0 --port 8080