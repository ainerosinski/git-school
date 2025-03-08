import random

def get_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Use a dictionary to map numbers to code snippets
    code_snippets = {
        1: "print('Hello World!')",
        2: "for i in range(5):\n\tprint(i)",
        3: "numbers = [1, 2, 3, 4, 5]\nprint(numbers)",
        4: "if num > 3:\n\tprint('Number is greater than 3')",
        5: "while num < 10:\n\tnum += 1",
        6: "def add(x, y):\n\treturn x + y\nprint(add(3, 4))",
        7: "list = [1, 2, 3, 4, 5]\nfor i in list:\n\tprint(i)",
        8: "dict = {'a': 1, 'b': 2, 'c': 3}\nfor key, value in dict.items():\n\tprint(key, value)",
        9: "try:\n\tnum = int(input('Enter a number: '))\nexcept ValueError:\n\tprint('Invalid input')",
        10: "with open('data.txt', 'r') as file:\n\tfor line in file:\n\t\tprint(line.strip())"
    }

    # Return the corresponding code snippet based on the random number generated
    return code_snippets[num]