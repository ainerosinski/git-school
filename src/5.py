import random 
  
def get_random_number(low: int, high: int): 
    return random.randint(low, high) 
  
print(get_random_number(1, 5))