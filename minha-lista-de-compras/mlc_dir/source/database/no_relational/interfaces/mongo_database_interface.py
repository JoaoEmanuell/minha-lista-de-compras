from abc import ABC, abstractmethod
from typing import Type, Dict, Any, Union, List
from mongoengine import Document, ObjectIdField


class MongoDatabaseInterface(ABC):
    """Mongo database interface base"""

    @abstractmethod
    def __init__(
        self,
        database_name: str = None,
        host: str = None,
        port: int = None,
        username: str = None,
        password: str = None,
    ) -> None:
        """Mongo database interface

        Args:
            database_name (str): Database name.
            host (str): Url to access the host.
            port (int): Port to the host.
            username (str): Username to connect a database
            password (str): Password to connect a database.
        """

        raise NotImplementedError()

    @abstractmethod
    def insert_one(self, model: Type[Document], data: Dict[str, Any]) -> bool:
        """Insert one data in database

        Args:
            model (Type[Document]): model is a collection object
            data (Dict[str, Any]): data corresponding to model

        Returns:
            bool: True if no problem, else false
        """
        raise NotImplementedError()

    @abstractmethod
    def select(
        self, model: Type[Document], data: Dict[str, Any]
    ) -> Union[List[Dict[str, Any]], list]:
        """Select data in database

        Args:
            model (Type[Document]): model is a collection object
            data (Dict[str, Any]): data corresponding to model
        Returns:
            Union[List[Dict[str, Any]], list]: List with dicts or empty list
        """
        raise NotImplementedError()

    @abstractmethod
    def update_one(
        self, id: Type[ObjectIdField], model: Type[Document], data: Dict[str, Any]
    ) -> bool:
        """Update one register on database

        Args:
            id (Type[ObjectIdField]): Id from register, mongo id
            model (Type[Document]): model is a collection object

        Returns:
            bool: True if no problem, else false
        """

        raise NotImplementedError()

    @abstractmethod
    def delete_one(self, id: Type[ObjectIdField], model: Type[Document]) -> bool:
        """Delete one object from database

        Args:
            id (Type[ObjectIdField]): Id from register, mongo id
            model (Type[Document]): model is a collection object

        Returns:
            bool: True if no problem, else false
        """
        raise NotImplementedError()
