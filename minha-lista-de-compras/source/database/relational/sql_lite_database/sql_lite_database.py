from typing import List, Dict, Any, Type
from pathlib import Path
from os.path import join
from orm_sqlite import Model, Database

from ..interfaces import SQLiteDatabaseInterface

class SQLiteDatabase(SQLiteDatabaseInterface):
    def __init__(self) -> None:
        path = join(Path().absolute(), 'database.db')
        self.__connection = self.create_connection(path)

    def create_connection(self, database_path: str) -> Type[Database]:
        if not database_path.endswith('db'):
            return Database(f'{database_path}.db')
        return Database(database_path)

    def select(self, model: Type[Model] = None, connection: Type[Database] = None, **data) -> List[Dict[str, Any]]:
        pass

    def update_one(self, id: str = None, model: Type[Model] = None, data: Dict[str, Any] = None, connection: Type[Database] = None) -> bool:
        pass

    def insert_one(self, model: Type[Model] = None, data: Dict[str, Any] = None, connection: Type[Database] = None) -> bool:
        if connection == None:
            connection = self.__connection
        
        model.objects.backend = connection
        result = model(data)
        result.save()

    def delete_one(self, id: str = None, model: Type[Model] = None, connection: Type[Database] = None) -> bool:
        pass