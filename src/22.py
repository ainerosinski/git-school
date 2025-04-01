def fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence of n numbers.
    
    Parameters:
    n (int): The length of the Fibonacci sequence to generate
    
    Returns:
    list: A list containing the first n numbers in the Fibonacci sequence
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

# Example usage
n = 10
print(fibonacci_sequence(n))
