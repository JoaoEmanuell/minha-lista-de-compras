from typing import Type, Dict, Any, Union, List
from json import loads

from mongoengine import Document, ObjectIdField, connect

from ..interfaces import MongoDatabaseInterface

class MongoDatabase(MongoDatabaseInterface):
    def __init__(self, database_name: str = None, host: str = None, port: int = None, username: str = None, password: str = None) -> None:
        connect(
            database_name,
            host=host,
            port=int(port),
            username=username,
            password=password
        )

    def insert_one(self, model: Type[Document], data: Dict[str, Any]) -> bool:
        try:
            model(**data).save()
            return True
        except:
            return False

    def select(self, model: Type[Document], data: Dict[str, Any]) -> Union[List[Dict[str, Any]], list]:
        try:
            obj_data: Document = model.objects(**data)
            return loads(obj_data.to_json())
        except:
            return []

    def update_one(self, id: Type[ObjectIdField], model: Type[Document], data: Dict[str, Any]) -> bool:
        try:
            id_validated = self.private_validate_id(id)
            model.objects(id=id_validated).update_one(**data)
            return True
        except:
            return False

    def delete_one(self, id: Type[ObjectIdField], model: Type[Document]) -> bool:
        try:
            id_validated = self.private_validate_id(id)
            model.objects(id=id_validated).delete()
            return True
        except:
            return False

    def private_validate_id(self, id: Union[Dict[str, str], str]) -> str:
        if type(id) != str:
            return id['$oid']
        return id