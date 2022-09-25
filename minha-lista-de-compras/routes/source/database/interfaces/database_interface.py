from abc import ABC, abstractmethod
from typing import List, Dict, Any

class DatabaseInterface(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def select(self, fields: List[Any], table: str, 
    data: Dict[str, Any]) -> List[Any]:
        raise NotImplementedError()

    @abstractmethod
    def update_one(self, id: str, table: str, 
    data: Dict[str, Any]) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def insert_one(self, fields: List[Any], table: str, 
    data: Dict[str, Any]) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self, id: str, table: str) -> bool:
        raise NotImplementedError()