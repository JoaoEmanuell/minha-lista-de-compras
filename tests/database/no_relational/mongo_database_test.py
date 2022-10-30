from sys import path
path.append('..')

from mlc.source import ListModel, Factory, MongoDatabaseInterface

def test_answer():
    id_user = 1
    list_name = 'Test List'
    mongo: MongoDatabaseInterface = \
        Factory().get_representative(MongoDatabaseInterface) # Object

    # Insert
    ## Valid

    data = {
        'id_user': id_user,
        'list_name': list_name,
        'data': ['1', '2', '3']
    }
    result = mongo.insert_one(ListModel, data)
    assert result == True

    ## Invalid

    data = {
        'id_user': id_user,
        'list': [132]
    }
    result = mongo.insert_one(ListModel, data)
    assert result == False

    # Select

    ## Valid
    data = {
        'id_user': id_user
    }
    result = mongo.select(ListModel, data)
    _id = result[0]['_id']
    assert result != []

    ## Invalid
    data = {
        'id_user': -1000
    }
    result = mongo.select(ListModel, data)
    assert result == []

    # Update

    ## Valid
    data = {
        'data': ['1', '3', '2']        
    }
    result = mongo.update_one(_id, ListModel, data)
    assert result == True

    ## Invalid 

    result = mongo.update_one(-1, ListModel, data)
    assert result == False

    # Delete

    result = mongo.delete_one(_id, ListModel)
    assert result == True