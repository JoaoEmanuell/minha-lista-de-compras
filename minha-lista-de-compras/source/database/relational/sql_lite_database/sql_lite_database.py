from typing import List, Dict, Any, Tuple, Type, Union
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

    def select(self, model: Type[Model]=..., connection: Type[Database]=..., \
        fields: List[str]=None, where: Dict[str, Any]=None) \
            -> Union[List[Dict[str, Any]], list]:
        
        try:
            connection = self.private__check_connection(connection)
            model.objects.backend = connection
            full_data: List[dict]=model.objects.all()

            # Validations
            if fields == None: # no fields
                raise Exception("Empty fields")

            if where == None: # no where
                return full_data
    
            if type(fields) != list:
                fields = [fields]
            
            available_dicts_tuple: Tuple[dict]=()
            where_size = len(where)
            
            # Select ... from Model where...

            for full_data_dict in full_data:
                count_where_in_dict = 0
                for key, value in full_data_dict.items():
                    if key in where:
                        if value == where[key]:
                            count_where_in_dict += 1
                if count_where_in_dict == where_size:
                    available_dicts_tuple += (full_data_dict, )

            # Filter fields

            if fields == ['*']: # all
                return [*available_dicts_tuple]
            
            fields_dict_tuple: Tuple[dict]=()

            for available_dict in available_dicts_tuple:
                fields_dict: Dict[str, Any]={}

                for field in fields:
                    if field in available_dict: # Take only available fields
                        fields_dict[field]= available_dict[field]

                fields_dict_tuple += (fields_dict, )

            return [*fields_dict_tuple]

        except:
            return []

    def update_one(self, id: int=..., model: Type[Model]=..., \
        data: Dict[str, Any]=..., connection: Type[Database]=...) -> bool:
        
        try: 
            connection = self.private__check_connection(connection)
            model.objects.backend = connection
            model({'id': id, **data}).update()
            return True

        except:
            return False

    def insert_one(self, model: Type[Model]=..., data: Dict[str, Any]=..., \
        connection: Type[Database]=...) -> bool:
        
        try:
            connection = self.private__check_connection(connection)
            model.objects.backend = connection
            result = model(data)
            result.save()
            return True
        except:
            return False

    def delete_one(self, id: int=None, model: Type[Model]=..., \
        connection: Type[Database]=...) -> bool:
        try:
            if type(id) != int:
                raise Exception

            id = abs(id)
            connection = self.private__check_connection(connection)
            model.objects.backend = connection
            model.objects.get(pk=id).delete()
            return True

        except:
            return False

    def private__check_connection(self, connection: Type[Database]) \
        -> Type[Database]:
        if connection == None:
            connection = self.__connection
        return connection