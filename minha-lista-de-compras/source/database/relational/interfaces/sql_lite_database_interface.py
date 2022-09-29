from abc import abstractmethod
from typing import Type, List, Dict, Any, Dict

from orm_sqlite import Database, Model

from .database_interface import DatabaseInterface

class SQLiteDatabaseInterface(DatabaseInterface):
    @abstractmethod
    def create_connection(self, database_path: str) -> Type[Database]:
        raise NotImplementedError()

    @abstractmethod
    def select(self, model: Type[Model]=None, connection: Type[Database]=None, **data) -> List[Dict[str, Any]]:
        raise NotImplementedError()

    @abstractmethod
    def update_one(self, id: int=None, model: Type[Model]=None, data: Dict[str, Any]=None, connection: Type[Database]=None) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def insert_one(self, model: Type[Model]=None, data: Dict[str, Any]=None, connection: Type[Database]=None) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self, id: int=None, model: Type[Model]=None, connection: Type[Database]=None) -> bool:
        raise NotImplementedError()