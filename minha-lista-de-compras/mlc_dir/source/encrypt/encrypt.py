from typing import List, Tuple
from cryptography.fernet import Fernet

from .interfaces import EncryptInterface


class Encrypt(EncryptInterface):
    def __init__(self, key: str) -> None:
        self.__encode = "UTF-8"
        byte_key = bytes(key, encoding=self.__encode)
        try:
            self.__fernet = Fernet(byte_key)
        except:
            raise Exception("Invalid Key")

    def encrypt(self, data: List[str]) -> List[str]:
        data_tuple: Tuple[str] = (*data,)
        encrypt_data = ()

        for string in data_tuple:
            encrypt_data += (
                self.__fernet.encrypt(self.pr__encode_string(string)).decode(
                    self.__encode
                ),
            )

        return [*encrypt_data]

    def decrypt(self, data: List[str]) -> List[str]:
        data_tuple: Tuple[str] = (*data,)
        decrypt_data = ()

        for string in data_tuple:
            decrypt_data += (
                self.__fernet.decrypt(self.pr__encode_string(string)).decode(
                    self.__encode
                ),
            )

        return [*decrypt_data]

    def pr__encode_string(self, string: str) -> bytes:
        # Private method to transform string in byte string
        return string.encode(self.__encode)
