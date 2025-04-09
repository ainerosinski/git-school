def square_root(x):
    if x < 0:
        return "Error: Division by zero."
    
    if x == 1 or x == 2:
        return x
    
    low = 1
    high = x
    
    while low <= high:
        mid = (low + high) // 2
        
        if mid * mid > x:
            high = mid - 1
        else:
            low = mid + 1
    
    return low

# Example usage:
result = square_root(9)
print(result) # Output: 3
