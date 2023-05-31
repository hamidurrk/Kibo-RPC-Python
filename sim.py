def generate_array(target):
    x = sorted(target)
    print(x)

    arr1 = [0, 0, 0]

    for i in range(3):
        if target[i] <= x[0]:
            arr1[i] = target[i]
            continue
        arr1[i] = x[0]


    arr2 = [0, 0, 0]

    for i in range(3):
        if target[i] <= x[1]:
            arr2[i] = target[i]
            continue
        arr2[i] = x[1]

    arr3 = [0, 0, 0]

    for i in range(3):
        if target[i] <= x[2]:
            arr3[i] = target[i]
            continue
        arr3[i] = x[2]
    
    arr = [arr1, arr2, arr3]
    
    return arr

position = generate_array([7, 5, 13])
print(position)
