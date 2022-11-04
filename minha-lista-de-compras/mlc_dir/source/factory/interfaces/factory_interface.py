from abc import ABC, abstractmethod
from typing import Type, Union

class FactoryInterface(ABC):
    @abstractmethod
    def get_representative(self, interface : Type[ABC]) -> Union[Type[ABC], object]:
        """Get Representative get a object correspondent to the interface

        Args:
            interface (Type[ABC]): Interface

        Returns:
            Union[Type[ABC], object]: Class not instantiated or object from class
        """
        raise NotImplementedError()