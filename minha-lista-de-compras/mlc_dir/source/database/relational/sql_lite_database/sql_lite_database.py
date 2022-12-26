from typing import List, Dict, Any, Union

from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.query import Query
from flask_sqlalchemy.model import Model

from ..interfaces import SQLiteDatabaseInterface


class SQLiteDatabase(SQLiteDatabaseInterface):
    def __init__(self) -> None:
        pass

    def select(
        self,
        connection: SQLAlchemy = None,
        model: Model = None,
        fields: List[str] = [],
        where: Dict[str, Any] = None,
    ) -> Union[List[List[Dict[str, Any]]], list]:

        try:
            result = []

            if fields == None:
                fields = ("*",)  # type: ignore

            if type(fields) != list or type(fields) != tuple:
                fields = (fields,)

            query: Query = connection.session.query(model)

            if where != None:
                for key, value in where.items():
                    query = query.filter(getattr(model, key) == value)
            else:
                query = query
                print(f"Query: {query}")

            result = self.private__transform_select_in_list(query)
            print(f"Result: {result}")
            if fields != ("*",):

                print(f"Select fields {fields[0]}")

                result = self.private__select_fields(fields[0], result)

            print(f"result : {result}")
            if result == [[{}]]:
                result = []

            return result

        except Exception as err:
            print(f"Error: {err}")
            return []

    def update_one(
        self,
        connection: SQLAlchemy = None,
        id: int = None,
        model: Model = None,
        data: Dict[str, Any] = None,
    ) -> bool:

        try:
            model.query.filter_by(id=id).update(data)
            connection.session.commit()
            return True
        except Exception as err:
            print(err)
            return False

    def insert_one(
        self,
        connection: SQLAlchemy = None,
        model: Model = None,
        data: Dict[str, Any] = None,
    ) -> bool:

        try:
            new_data = model(**data)
            connection.session.add(new_data)
            connection.session.commit()
            return True
        except Exception as err:
            print(err)
            return False

    def delete_one(
        self, connection: SQLAlchemy = None, id: int = None, model: Model = None
    ) -> bool:

        try:
            user = model.query.filter_by(id=id).first()
            connection.session.delete(user)
            connection.session.commit()
            return True
        except Exception as err:
            print(f"Delete error: {err}")
            return False

    def private__transform_select_in_list(
        self, query: Query
    ) -> List[List[Dict[str, Any]]]:

        result_list: List[Dict[str, Any]] = [u.__dict__ for u in query.all()]

        new_result_list = []

        for res_list in result_list:
            tmp_dict = {}
            for key, value in res_list.items():
                if key == "_sa_instance_state":
                    pass
                else:
                    tmp_dict[key] = value
            new_result_list.append([tmp_dict])

        return new_result_list

    def private__select_fields(
        self, fields: list[str], data: list[list[dict[str, Any]]]
    ) -> list[list[dict[str, Any]]]:
        result = []

        for list_with_list_dict in data:
            list_with_dict = list_with_list_dict[0]
            tmp_dict_result = {}
            for key, value in list_with_dict.items():
                if key in fields:
                    tmp_dict_result[key] = value
            result.append([tmp_dict_result])

        return result
