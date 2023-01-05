from sys import path

path.append("..")

from mlc.mlc_dir import UserModel, Factory, SQLiteDatabaseInterface, sql_db, app


def test_answer():
    ID = 1

    sql_lite: SQLiteDatabaseInterface = Factory().get_representative(
        SQLiteDatabaseInterface
    )  # Object

    sql_db.init_app(app)
    with app.app_context():
        sql_db.create_all()
        # Insert

        ## Valid insert
        data = {"username": "test", "password": "test"}
        result = sql_lite.insert_one(sql_db, UserModel, data)
        assert result == True

        ## Invalid insert
        data_invalid = {"username": "test"}
        result = sql_lite.insert_one(sql_db, UserModel, data_invalid)
        assert result == False

        # Update

        ## Valid update
        data = {"username": "test2", "password": "test2"}
        result = sql_lite.update_one(sql_db, ID, UserModel, data)
        assert result == True

        ## Invalid update
        data_invalid = {"user": "test"}
        result = sql_lite.update_one(sql_db, ID, UserModel, data_invalid)
        assert result == False

        # Select
        ## Valid select
        where = {"username": "test2"}
        fields = "*"
        result = sql_lite.select(sql_db, UserModel, fields, where)
        assert result[0] == [{"id": 1, "username": "test2", "password": "test2"}]

        ## Valid select with fields
        fields = "username"
        result = sql_lite.select(sql_db, UserModel, fields, where)
        assert result == [[{"username": "test2"}]]

        ## Invalid select
        where = {"username": "test"}
        result = sql_lite.select(sql_db, UserModel, fields, where)
        assert result == []

        ## Sql injection
        where = {"id": "105 OR 1=1"}
        result = sql_lite.select(sql_db, UserModel, fields, where)
        assert result == []

        ## No where
        result = sql_lite.select(sql_db, UserModel, fields)
        assert result == [[{"username": "test2"}]]

        ## No fields
        result = sql_lite.select(sql_db, UserModel)
        assert result == []

        ## No connection
        result = sql_lite.select(model=UserModel)
        assert result == []

        ## No model
        result = sql_lite.select()
        assert result == []

        # Delete
        ## Valid delete
        result = sql_lite.delete_one(sql_db, ID, UserModel)
        assert result == True

        ## Invalid delete
        result = sql_lite.delete_one(sql_db, ID, UserModel)
        assert result == False
