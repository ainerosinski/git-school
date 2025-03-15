import random

def get_random_python_code():
    # Generate a random number between 1 and 5
    num = random.randint(1, 5)

    # Return a string based on the number generated
    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "for i in range(5):\n\tprint(i)"
    elif num == 3:
        return "my_list = [1, 2, 3, 4, 5]\nfor item in my_list:\n\tprint(item)"
    elif num == 4:
        return "def add(x, y):\n\treturn x + y\nprint(add(3, 5))"
    else:
        return "while True:\n\tprint('Hello World!')"