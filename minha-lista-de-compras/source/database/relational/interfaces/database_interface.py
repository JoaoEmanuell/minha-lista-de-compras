from abc import ABC, abstractmethod
from typing import Any

class DatabaseInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def select(self) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def update_one(self) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def insert_one(self) -> Any:
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self) -> Any:
        raise NotImplementedError()