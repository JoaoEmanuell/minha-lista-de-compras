from sys import path
from os import environ as env

from dotenv import load_dotenv

path.append("..")

load_dotenv(dotenv_path="./.env")

from mlc.mlc_dir.source import Factory, EncryptInterface


def test_answer():
    fac = Factory()
    encrypt_key = env["ENCRYPTION_KEY"]
    encrypt = fac.get_representative(EncryptInterface)  # class
    encrypt: EncryptInterface = encrypt(encrypt_key)

    text_data = ["Hello World!"]
    encrypt_text_data = encrypt.encrypt(text_data)

    assert type(encrypt_text_data) == list
    assert len(encrypt_text_data) == 1

    decrypt_text_data = encrypt.decrypt(encrypt_text_data)

    assert type(decrypt_text_data) == list
    assert len(decrypt_text_data) == 1
    assert decrypt_text_data == text_data
