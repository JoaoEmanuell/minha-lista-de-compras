from typing import Tuple, Type, Union
from abc import ABC

from .interfaces import FactoryInterface

from ..database import mongo, sql_lite
from ..hash import Hash
from ..encrypt import Encrypt

class Factory(FactoryInterface):
    def __init__(self) -> None:
        self.__representatives : Tuple[ABC] = (
            mongo, 
            sql_lite,
            Hash,
            Encrypt,
        )

    def get_representative(self, interface: Type[ABC]) \
        -> Union[Type[ABC], object]:
        for representative in self.__representatives:
            try:
                if issubclass(representative, interface):
                    return representative
            except TypeError:
                if isinstance(representative, interface):
                    return representative

        raise ValueError(f"No representative found for interface: {interface}")