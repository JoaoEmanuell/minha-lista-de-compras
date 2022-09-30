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

    # Model

    data = {'id': id, 'username': 'test', 'password': 'test'}
    result = sql_lite.insert_one(UserModel, data, connection)
    assert result == True

    # Update

    data = {'username': 'test2', 'password': 'test2'}
    result = sql_lite.update_one(id, UserModel, data, connection)
    assert result == True

    # Delete
    
    result = sql_lite.delete_one(id, UserModel, connection)
    assert result == True

test_answer()