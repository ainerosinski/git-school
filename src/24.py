def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = calculate_sum(numbers)
print(result)  # Output: 15
