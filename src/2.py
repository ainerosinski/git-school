import random

def get_random_code(length):
    characters = "abcdefghijklmnopqrstuvwxyz" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789"
    result = ""
    for i in range(length):
        result += characters[random.randint(0, len(characters) - 1)]
    return result
