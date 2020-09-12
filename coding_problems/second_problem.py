import sys
import numpy

class linear():
    def __init__(self, a_val, b_val, c_val):
        a = int(a_val) 
        b = int(b_val) 
        c = int(c_val)
        
        #find y-intercept
        self.y_int = -c / b 

        #find slope
        self.slope = -a / b 

        self.all_points = []
    
    def generate_points(self):
        for i in numpy.arange(-2.5, 1, 0.5):
            self.all_points.append((i, self.y_int - self.slope * i))
        for i in numpy.arange(1, 3, 0.5):
            self.all_points.append((i, self.y_int + self.slope * i))
        return self.all_points

class quadratic():
    def __init__(self, a_val, b_val, c_val):
        self.a = int(a_val) 
        self.b = int(b_val) 
        self.c = int(c_val)
        
        #find x coordinate of vertex
        self.x_vertex = -self.b / (2 * self.a)

        #find y coordinate of vertex
        self.y_vertex = ((self.a * self.x_vertex ** 2) + (self.b * self.x_vertex) + self.c)

        self.vertex = (self.x_vertex, self.y_vertex)

        self.left_points = []
        self.right_points = []
    
    def right(self):
        self.right_points.append(self.vertex)

        y = self.y_vertex
        j = 1
        for i in numpy.arange(self.x_vertex + 0.5, self.x_vertex + 3, 0.5):
            y += self.a * j / 4
            self.right_points.append([i, y])
            j += 2

        return self.right_points

    def left(self): 
        y = self.y_vertex
        j = 1
        y_values = []
        for i in numpy.arange(self.x_vertex - 2.5, self.x_vertex, 0.5):
            y += self.a * j / 4
            self.left_points.append([i])
            y_values.append(y)
            j += 2

        y_values.reverse()
        e = 0
        for i in y_values:
            self.left_points[e].append(i)
            e += 1

        return self.left_points


while True:
    relationship = input('''Which table for a relationship would you like to see?
    1. Linear
    2. Quadratic\n''')
    
    if relationship == '1':
        print("For an equation in the form: ax + by + c = 0")
        a_val = input("Enter the 'a' value: ")
        b_val = input("Enter the 'b' value: ")
        c_val = input("Enter the 'c value: ")
        
        line = linear(a_val, b_val, c_val)
        points = line.generate_points()

    elif relationship == '2':
        print("For an equation in the form: y = ax^2 + bx + c")
        a_val = input("Enter the 'a' value: ")
        b_val = input("Enter the 'b' value: ")
        c_val = input("Enter the 'c value: ")

        parabola = quadratic(a_val, b_val, c_val)
        first_points = parabola.left()
        last_points = parabola.right()
        points = first_points + last_points

    else: 
        break

    print("(x value, y value)")
    for i in points:
        print(f"({i[0]}, {i[1]})")

    response = input("Would you like to try another one? Y/N\n")
    if response.upper() == 'Y':
        continue 
    else:
        break


sys.exit()