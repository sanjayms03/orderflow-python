import hashlib
import random
import string

def hash_password(password):
    return hashlib.md5(password.encode("utf-8")).hexdigest()

def temporary_code(length=8):
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))
