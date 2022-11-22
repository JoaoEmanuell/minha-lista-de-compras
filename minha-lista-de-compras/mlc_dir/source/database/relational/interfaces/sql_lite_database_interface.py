from abc import abstractmethod
from typing import List, Dict, Any, Dict, Union

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model

from .database_interface import DatabaseInterface

class SQLiteDatabaseInterface(DatabaseInterface):
    """Sql lite database interface"""

    @abstractmethod
    def select(self, connection: SQLAlchemy=None, model: Model=None, \
        fields: List[str]=[], where:Dict[str, Any]=None) -> \
            Union[List[List[Dict[str, Any]]], list]:
        """Select [fields] in [model] [where]

        Args:
            model (Model): Model to realize a select. Defaults to None.
            connection (Type[db]): Connection. Defaults to None.
            fields (List[str]): Fields, if '*' then all fields will be returned. Defaults to [].
            where (Dict[str, Any]): Where, if '*' then all records will be returned. Defaults to None.

        Returns:
            Union[List[Dict[str, Any]], list]: List with dict of records. Or empty list
        """        
        raise NotImplementedError()

    @abstractmethod
    def update_one(self, connection: SQLAlchemy=None, id: int=None, \
        model: Model=None, data: Dict[str, Any]=None) -> bool:
        """Update [model] set [data] where [id = id]

        Args:
            id (int): id to record. Defaults to None.
            model (Model): Model to realize a update. Defaults to None.
            data (Dict[str, Any]): Data to realize a update. Defaults to None.
            connection (Type[db]): Connection. Defaults to None.

        Returns:
            bool: True if successfully, else False
        """        
        raise NotImplementedError()

    @abstractmethod
    def insert_one(self, connection: SQLAlchemy=None, model: Model=None, \
        data: Dict[str, Any]=None) -> bool:
        """insert into [model] values [data]

        Args:
            model (Model): Model to realize a insert. Defaults to None.
            data (Dict[str, Any]): Data to realize a insert. Defaults to None.
            connection (Type[db]): Connection. Defaults to None.

        Returns:
            bool: True if successfully, else False
        """        
        raise NotImplementedError()

    @abstractmethod
    def delete_one(self, connection: SQLAlchemy=None, id: int=None, \
        model: Model=None) -> bool:
        """delete from [model] where [id = id]

        Args:
            id (int): id to record. Defaults to None.
            model (Model): Model to realize a delete. Defaults to None.
            connection (Type[db]): Connection. Defaults to None.

        Returns:
            bool: True if successfully, else False
        """        
        raise NotImplementedError()