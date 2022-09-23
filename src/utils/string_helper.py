import random
import string
import uuid


def random_string(length):
    char = string.ascii_lowercase+string.digits+string.ascii_uppercase
    return ''.join(random.choice(char) for i in range(length))


def get_uuid():
    uuid_str = str(uuid.uuid4())
    return uuid_str
