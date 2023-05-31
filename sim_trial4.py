from vpython import *
from time import *

scene = canvas(width = 1920, height = 1080)

cylinder(pos=vector(0, 0, 0), axis=vector(20, 0, 0), color=color.red, radius=0.05)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 20, 0), color=color.green, radius=0.05)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 20), color=color.blue, radius=0.05)

floor = box(pos = vector(0, -10, 0), color = color.white, length = 50, height = 0.1, width = 50)
robot = box(color = color.yellow, length = 1, height = 1, width = 1)
position = [0, 0, 0]
target = [7, 5, 13]

class Koz:
    def __init__(self, i, j, k, l, h, w):
        self.box =  box(pos = vector(i, j, k), color = color.red, length = l, height = h, width = w)
class Kiz:
    def __init__(self, p):
        self.box =  box(pos = vector(p[0], p[1], p[2]), color = color.green, length = 0.5, height = 0.5, width = 0.5)
kiz1 = Kiz(target)
koz1 = Koz(-1, 6, 10, 20, 10, 1)

inc = 0.1

def generate_vector_path(target):
    x = sorted(target)

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

def three_dim_man(pos, tar):
    tem = [0, 0, 0]
    d = [x - y for x, y in zip(tar, pos)]
    dx = next((element for element in d if element != 0), None)

    if dx != None:
        non_zero_indices = [i for i, x in enumerate(d) if x != 0]

        for i in range(len(tem)):
            if i in non_zero_indices:
                tem[i] += 1

        for i in range(dx):
            step = [x + y for x, y in zip(pos, tem)]
            pos = step
            print(f"Step: {step}")
            robot.pos = vector(step[0], step[1], step[2])
            rate(2)
    
checkpoints = generate_vector_path(target)
print(checkpoints)
while True:
    three_dim_man(position, position)
    three_dim_man(position, checkpoints[0])
    three_dim_man(checkpoints[0], checkpoints[1])
    three_dim_man(checkpoints[1], checkpoints[2])
    

