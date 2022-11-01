from sys import path

path.append('..')

from mlc.source import Factory, DatabaseInterface
from mlc.source.factory.interfaces import FactoryInterface

def test_answer():
    fac = Factory()
    assert isinstance(fac, FactoryInterface)

    database = fac.get_representative(DatabaseInterface)

    assert isinstance(database, DatabaseInterface)