from abc import ABC, abstractmethod
from typing import Any

class DatabaseInterface(ABC):
    """ Base interface for all databases class"""
    @abstractmethod
    def __init__(self) -> None:
        """Init"""        
        raise NotImplementedError()

    @abstractmethod
    def select(self) -> Any:
        """Select"""
        raise NotImplementedError()

    @abstractmethod
    def update_one(self) -> Any:
        """Update one"""
        raise NotImplementedError()

    @abstractmethod
    def insert_one(self) -> Any:
        """Insert one"""
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self) -> Any:
        """Delete one"""
        raise NotImplementedError()