import numpy as np

vector1 = np.array([1, 2, 3])
print(vector1)

def find_smallest(input):
    numbers = [num for num in input if num != 0]
    
    if len(numbers) == 0:
        return None  
    
    smallest = min(numbers)
    return smallest

def update_position(target):
    position = [0, 0, 0]
    targetvector = np.array(target)
    min_val = find_smallest(target)
    print(min_val)

    return position


target_position = [7, 5, 13]
final_position = update_position(target_position)
