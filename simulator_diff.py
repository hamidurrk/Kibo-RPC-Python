# from vpython import *
# from time import *

# cylinder(pos=vector(0, 0, 0), axis=vector(20, 0, 0), color=color.red, radius=0.05)
# cylinder(pos=vector(0, 0, 0), axis=vector(0, 20, 0), color=color.green, radius=0.05)
# cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 20), color=color.blue, radius=0.05)

# floor = box(pos = vector(0, -10, 0), color = color.white, length = 50, height = 0.1, width = 50)
# robot = box(color = color.white, length = 1, height = 1, width = 1)
# kiz = box(color = color.green, length = 1, height = 1, width = 1)
# class Koz:
#     def __init__(self, i, j, k, l, h, w):
#         self.box =  box(pos = vector(i, j, k), color = color.red, length = l, height = h, width = w)

# i = 0
# j = 0
# k = 0

# ti = 7
# tj = 6
# tk = 13

# inc = 0.1

# kiz.pos = vector(ti, tj, tk)
# koz1 = Koz(-1, 6, 10, 20, 10, 1)

def update_position(target):
    position = [0, 0, 0]
    checkpoint = [0, 0, 0]
    x = sorted(target)
    print(x)

    if checkpoint[0] != x[0]:
        checkpoint[0] = x[0]
    if checkpoint[1] != x[0]:
        checkpoint[1] = x[0]
    if checkpoint[2] != x[0]:
        checkpoint[2] = x[0]
    print(checkpoint)

    index = target.index(x[0])
    
    if 0 != index & checkpoint[0] != x[1]:
        checkpoint[0] = x[1]
    if 1 != index & checkpoint[1] != x[1]:
        checkpoint[1] = x[1]
    if 2 != index & checkpoint[2] != x[1]:
        checkpoint[2] = x[1]
    print(checkpoint)

    index1 = target.index(x[1])
    
    if 0 != index & 0 != index1 & checkpoint[0] != x[1]:
        checkpoint[0] = x[1]
    if 1 != index & checkpoint[1] != x[1]:
        checkpoint[1] = x[1]
    if 2 != index & checkpoint[2] != x[1]:
        checkpoint[2] = x[1]
    print(checkpoint)
  
    return position

# Test the function
target_position = [7, 5, 13]
final_position = update_position(target_position)


    
    
        