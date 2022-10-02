from pathlib import Path
from os.path import join, exists

from sys import path
path.append('..')

from mlc.source import sql_lite as sql_lite_global
from mlc.source import UserModel

def test_answer():
    absolute_path = Path().absolute()
    path_to_db = join(absolute_path, 'database.db')
    id = 1

    sql_lite = sql_lite_global

    # Create connection
    connection = sql_lite.create_connection(path_to_db)
    assert exists(path_to_db)

    # Insert

    data = {'id': id, 'username': 'test', 'password': 'test'}
    result = sql_lite.insert_one(UserModel, data, connection)
    assert result == True

    # Update

    data = {'username': 'test2', 'password': 'test2'}
    result = sql_lite.update_one(id, UserModel, data, connection)
    assert result == True

    # Select
    ## Valid select
    where = {'username': 'test2'}
    fields = '*'
    result = sql_lite.select(UserModel, connection, fields, where)
    assert result == [{'id': 1, 'username': 'test2', 'password': 'test2'}]

    ## Invalid select
    where = {'username': 'test'}
    result = sql_lite.select(UserModel, connection, fields, where)
    assert result == []

    ## Sql injection
    where = {'id': '105 OR 1=1'}
    result = sql_lite.select(UserModel, connection, fields, where)
    assert result == []

    ## No where
    result = sql_lite.select(UserModel, connection, fields)
    assert result == [{'id': 1, 'username': 'test2', 'password': 'test2'}]

    ## No fields
    result = sql_lite.select(UserModel, connection)
    assert result == []

    ## No connection
    result = sql_lite.select(UserModel)
    assert result == []

    ## No model
    result = sql_lite.select()
    assert result == []

    # Delete
    ## Valid delete
    result = sql_lite.delete_one(id, UserModel, connection)
    assert result == True
    
    ## Invalid delete
    result = sql_lite.delete_one(model=UserModel, connection=connection)
    assert result == False
