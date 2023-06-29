from vpython import *
from time import *

class Draw:
    def __init__(self, canvas_width, canvas_height, length, factor = 100):
        scene = canvas(width = canvas_width, height = canvas_height, )
        scene.up = vector(0, 0, -1)    
        scene.forward = vector(0, -1, 0)    
        scene.right = vector(-1, 0, 0) 

        self.factor = factor
        
        self.ceiling_position = [0, 0, 0]
        self.floor_position = [0, 0, 6]
        self.wall_position = [12, 0, 0]

        self.point_size = [0.1, 0.1, 0.1]

        cylinder(pos=vector(0, 0, 0), axis=vector(length, 0, 0), color=color.red, radius=5)
        cylinder(pos=vector(0, 0, 0), axis=vector(0, length, 0), color=color.green, radius=5)
        cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, length), color=color.blue, radius=5)
    
    def multiply_by_factor(self, lst):
        cm_list = [num * self.factor for num in lst]
        return cm_list
    
    def box(self, corner, size, color, opacity):
        self.size = self.multiply_by_factor(size)
        self.color = color
        self.opacity = opacity
        center = self.multiply_by_factor([corner[0] + size[0] / 2, -(corner[1] + size[1] / 2), corner[2] + size[2] / 2])

        box(pos=vector(*center), size= vector(*self.size), color=self.color, opacity = self.opacity)

    def ceiling(self, length, width):
        self.box(self.ceiling_position, [length, width, -0.1], color=color.white, opacity=0.5)
    
    def floor(self, length, width):
        self.box(self.floor_position, [length, width, 0.1], color=color.white, opacity=0.5)

    def wall(self, width):
        self.box(self.wall_position, [0.1, width, self.floor_position[2]], color=color.white, opacity=0.5)

    def koz(self, dict):
        for key in dict:
            value = dict[key]
            self.min = value[0]
            self.max = value[1]

            self.size = [self.max[0] - self.min[0], self.max[1] - self.min[1], self.max[2] - self.min[2]]
            self.box(self.min, [self.size[0], self.size[1], self.size[2]], color=color.red, opacity=1)
    
    def kiz(self, dict):
        for key in dict:
            value = dict[key]
            self.min = value[0]
            self.max = value[1]

            self.size = [self.max[0] - self.min[0], self.max[1] - self.min[1], self.max[2] - self.min[2]]
            self.box(self.min, [self.size[0], self.size[1], self.size[2]], color=color.blue, opacity=0.1)

    def start(self, start_position):
        self.box(start_position, self.point_size, color=color.cyan, opacity=1)
    
    def goal(self, goal_position):
        self.box(goal_position, self.point_size, color=color.magenta, opacity=1)

    def point(self, dict):
        for key in dict:
            value = dict[key]
            point = value
            print(point)
            self.box(point, self.point_size, color=color.orange, opacity=1)
    
    def target(self, dict):
        for key in dict:
            value = dict[key]
            target = value
            self.box(target, self.point_size, color=color.orange, opacity=1)

if __name__ == "__main__":
    canvas_width = 1920
    canvas_height = 1080 
    axes_length = 2000
    corridor_length = 20

    start_position = [9.815, -9.806, 4.293]
    goal_position = [11.143, -6.7607, 4.9654]

    point_dict = {
        1: ([11.2746, -9.92284, 5.2988]),
        2: ([10.612, -9.0709, 4.48])
    }

    target_dict = {
        1: ([11.2625, -10.58, 5.3625]),
        2: ([10.513384, -9.085172, 3.76203])
    }
    
    koz_dict = {
        1: ([10.783, -9.8899, 4.8385], [11.071, -9.6929, 5.0665]),
        2: ([10.8652, -9.0734, 4.3861], [10.9628, -8.7314, 4.6401])
    }

    kiz_dict = {
        1: ([10.3, -10.2, 4.32], [11.55, -6.0, 5.57]),
        2: ([9.5, -10.5, 4.02], [10.5, -9.6, 4.8])
    }

    draw = Draw(canvas_width, canvas_height, axes_length)
    #draw.ceiling(12, -corridor_length)
    draw.floor(12, -corridor_length)
    draw.wall(-corridor_length)

    draw.start(start_position)
    draw.goal(goal_position)
    draw.koz(koz_dict)
    draw.kiz(kiz_dict)
    draw.point(point_dict)
    draw.target(target_dict)
    
    while True:
        rate(60)

