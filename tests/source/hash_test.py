from sys import path

path.append("..")

from mlc.source import Factory, HashInterface


def test_answer():
    fac = Factory()
    hash: HashInterface = fac.get_representative(HashInterface)()
    assert isinstance(hash, HashInterface)

    text = "Hello World"
    hash_text = hash.generate_hash(text)
    assert hash.compare_hash(text, hash_text)
