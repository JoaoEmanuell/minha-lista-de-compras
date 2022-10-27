FROM nikolaik/python-nodejs:python3.11-nodejs19-alpine

RUN apk add --no-cache --upgrade bash

# Args and env

ARG USER=pn
ENV HOME=/home/$USER
ENV PATH="${PATH}:${HOME}/.local/bin"

# Sudo

RUN apk add --update sudo

USER $USER

RUN mkdir $HOME/app

WORKDIR "${HOME}/app"

# Normal user

## Python

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8080