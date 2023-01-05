from random import randint
from hashlib import sha256

random_number = str(randint(1, 1000000000000))
hash = sha256(random_number.encode("UTF-8")).hexdigest()
print(hash)
