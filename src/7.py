import numpy as np
def get_unique_elements(my_list):
    unique_elements = []
    for element in my_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

# Test case 1:
assert get_unique_elements([]) == []
# Test case 2:
assert get_unique_elements([1]) == [1]
# Test case 3:
assert get_unique_elements([1, 2, 3, 2, 1]) == [1, 2, 3]