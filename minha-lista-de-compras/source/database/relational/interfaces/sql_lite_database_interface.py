from abc import abstractmethod
from typing import Type, List, Dict, Any, Dict, Union

from orm_sqlite import Database, Model

from .database_interface import DatabaseInterface

class SQLiteDatabaseInterface(DatabaseInterface):
    """Sql lite database interface"""
    @abstractmethod
    def create_connection(self, database_path: str) -> Type[Database]:
        """Create a connection from db file

        Args:
            database_path (str): path to db file

        Returns:
            Type[Database]: orm_sqlite Database object
        """        
        raise NotImplementedError()

    @abstractmethod
    def select(self, model: Type[Model]=None, connection: Type[Database]=None, fields: List[str]=[], where:Dict[str, Any]=None) -> Union[List[Dict[str, Any]], list]:
        """Select [fields] in [model] [where]

        Args:
            model (Type[Model]): Model to realize a select. Defaults to None.
            connection (Type[Database]): Connection. Defaults to None.
            fields (List[str]): Fields, if '*' then all fields will be returned. Defaults to [].
            where (Dict[str, Any]): Where, if '*' then all records will be returned. Defaults to None.

        Returns:
            Union[List[Dict[str, Any]], list]: List with dict of records. Or empty list
        """        
        raise NotImplementedError()

    @abstractmethod
    def update_one(self, id: int=None, model: Type[Model]=None, data: Dict[str, Any]=None, connection: Type[Database]=None) -> bool:
        """Update [model] set [data] where [id = id]

        Args:
            id (int): id to record. Defaults to None.
            model (Type[Model]): Model to realize a update. Defaults to None.
            data (Dict[str, Any]): Data to realize a update. Defaults to None.
            connection (Type[Database]): Connection. Defaults to None.

        Returns:
            bool: True if successfully, else False
        """        
        raise NotImplementedError()

    @abstractmethod
    def insert_one(self, model: Type[Model]=None, data: Dict[str, Any]=None, connection: Type[Database]=None) -> bool:
        """insert into [model] values [data]

        Args:
            model (Type[Model]): Model to realize a insert. Defaults to None.
            data (Dict[str, Any]): Data to realize a insert. Defaults to None.
            connection (Type[Database]): Connection. Defaults to None.

        Returns:
            bool: True if successfully, else False
        """        
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self, id: int=None, model: Type[Model]=None, connection: Type[Database]=None) -> bool:
        """delete from [model] where [id = id]

        Args:
            id (int): id to record. Defaults to None.
            model (Type[Model]): Model to realize a delete. Defaults to None.
            connection (Type[Database]): Connection. Defaults to None.

        Returns:
            bool: True if successfully, else False
        """        
        raise NotImplementedError()