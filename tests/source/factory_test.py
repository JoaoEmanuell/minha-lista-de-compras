from sys import path

path.append("..")

from mlc.mlc_dir.source import Factory, DatabaseInterface, FactoryInterface


def test_answer():
    fac = Factory()
    assert isinstance(fac, FactoryInterface)

    database = fac.get_representative(DatabaseInterface)

    assert isinstance(database, DatabaseInterface)
