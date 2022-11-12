import string
from random import sample


def get_random_password(n=8) -> str:
    list_ = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
    password = "".join(sample(list_, n))
    return password


print(get_random_password())
