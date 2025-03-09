import random

def get_random_code():
    return "".join(str(random.randint(0, 9)) for i in range(8))