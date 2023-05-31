from vpython import *
from time import *

floor = box(pos = vector(0, -10, 0), color = color.white, length = 50, height = 0.1, width = 50)
robot = box(color = color.white, length = 1, height = 1, width = 1)
kiz = box(color = color.green, length = 1, height = 1, width = 1)

cylinder(pos=vector(0, 0, 0), axis=vector(20, 0, 0), color=color.red, radius=0.05)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 20, 0), color=color.green, radius=0.05)
cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 20), color=color.blue, radius=0.05)

i = 0
j = 0
k = 0

ti = 7
tj = 6
tk = 13

inc = 0.1

kiz.pos = vector(ti, tj, tk)

class Koz:
    def __init__(self, i, j, k, l, h, w):
        self.box =  box(pos = vector(i, j, k), color = color.red, length = l, height = h, width = w)

koz1 = Koz(-1, 6, 10, 20, 10, 1)

def find_smallest(a, b, c):
    numbers = [num for num in [a, b, c] if num != 0]
    
    if len(numbers) == 0:
        return None  
    
    smallest = min(numbers)
    return smallest

def count_zeros(a, b, c):
    count = 0
    if a == 0:
        count += 1
    if b == 0:
        count += 1
    if c == 0:
        count += 1
    return count

def three_dim_man(x, y, z, p, *str):
    while sqrt(x**2 + y**2 + z**2) < sqrt(p**2 + p**2 + p**2):
        for s in str:
            if s == 'i':
                x += inc
            if s == 'j':
                y += inc
            if s == 'k':
                z += inc        
        robot.pos = vector(x, y, z)
        print(f"{x}, {y}, {z}")
        rate(20)


while True: 
    a = min(ti, tj, tk)
    three_dim_man(i, j, k, a, 'i', 'j', 'k')
    print(f"{i}, {j}, {k}")

    di = ti - a
    dj = tj - a
    dk = tk - a

    numofzero = count_zeros(di, dj, dk)
    print(numofzero)
    if numofzero == 1:
        if di == 0:
            a = min(dj, dk)
            three_dim_man(i, j+dj, k+dk, a, 'j', 'k')
        if dj == 0:
            a = min(di, dk)
            print(f"{i}, {j}, {k}")
            three_dim_man(i+di, j, k+dk, a, 'i', 'k')
        if dk == 0:
            a = min(di, dj)
            three_dim_man(i+dj, j+dj, k, a, 'i', 'j')
    
    if numofzero == 2:
        if di != 0:
            a = di
            three_dim_man(i+dj, j, k, a, 'i')
        if dj != 0:
            a = dj
            three_dim_man(i, j+dj, k, a, 'j')
        if dk == 0:
            a = dk
            three_dim_man(i, j, k+dk, a, 'k')
    if numofzero == 3:
        pass
    



    
    
        