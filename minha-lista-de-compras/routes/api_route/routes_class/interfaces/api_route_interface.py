from abc import ABC, abstractmethod
from typing import Type, Dict, Any

from flask.wrappers import Request

from source.factory.interfaces import FactoryInterface


class ApiRouteInterface(ABC):
    """Api route interface to all routes class"""

    @abstractmethod
    def __init__(self, request: Type[Request], factory: Type[FactoryInterface]) -> None:
        """Init

        Args:
            request (Type[Request]): flask request
            factory (Type[FactoryInterface]): Factory to access others class using interfaces
        """
        raise NotImplementedError()

    @abstractmethod
    def run(self) -> Dict[str, Any]:
        """Run the api class

        Returns:
            Dict[str, Any]: Response, dict to convert in a json
        """
        raise NotImplementedError()
