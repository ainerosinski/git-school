import random

def get_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Check if the number is even or odd
    if num % 2 == 0:
        return f"print('The number {num} is even')"
    else:
        return f"print('The number {num} is odd')"
