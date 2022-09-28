from pathlib import Path
from os.path import join, exists

from sys import path
path.append('..')

from mlc.source import sql_lite as sql_lite_global

def test_answer():
    absolute_path = Path().absolute()
    path_to_db = join(absolute_path, 'database.db')

    sql_lite = sql_lite_global

    # Create connection
    sql_lite.create_connection(path_to_db)
    assert exists(path_to_db)