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

    def select(self, model: Type[Model]=None, connection: Type[Database]=None, **data) -> List[Dict[str, Any]]:
        pass

    def update_one(self, id: int=None, model: Type[Model]=None, data: Dict[str, Any]=None, connection: Type[Database]=None) -> bool:
        connection = self.private__check_connection(connection)

        try: 
            old_data: dict = model.objects.get(pk=id)
            new_data = old_data.copy()

            for key, value in data.items():
                new_data[key] = value
            
            self.delete_one(id, model, connection)
            self.insert_one(model, new_data, connection)
            return True

        except:
            return False

    def insert_one(self, model: Type[Model]=None, data: Dict[str, Any]=None, connection: Type[Database]=None) -> bool:
        connection = self.private__check_connection(connection)
        
        try:
            model.objects.backend = connection
            result = model(data)
            result.save()
            return True
        except:
            return False

    def delete_one(self, id: int=None, model: Type[Model]=None, connection: Type[Database]=None) -> bool:
        connection = self.private__check_connection(connection)

        try:
            model.objects.get(pk=id).delete()
            return True

        except (Exception, AttributeError) as error:
            print(error.with_traceback())
            return False

    def private__check_connection(self, connection: Type[Database]) \
        -> Type[Database]:
        if connection == None:
            connection = self.__connection
        return connection