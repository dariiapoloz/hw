import math
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        if (self.a + self.b <= self.c or
            self.a + self.c <= self.b or
            self.b + self.c <= self.a):
            return 0
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b
class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.h
class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def area(self):
        return 0
class Circle:
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return math.pi * self.r * self.r
shapes = []

def readfile(filename):
 with open(filename) as file:
    for line in file:
        parts = line.split()
        if len(parts) == 0:
            continue
        name = parts[0]
        nums = list(map(float, parts[1:]))
        if name == "Triangle":
            shapes.append(Triangle(nums[0], nums[1], nums[2]))
        elif name == "Rectangle":
            shapes.append(Rectangle(nums[0], nums[1]))
        elif name == "Parallelogram":
            shapes.append(Parallelogram(nums[0], nums[1], nums[2]))
        elif name == "Trapeze":
            shapes.append(Trapeze(nums[0], nums[1], nums[2], nums[3]))
        elif name == "Circle":
            shapes.append(Circle(nums[0]))
    return shapes
print("from input01.txt")
readfile("input01.txt")
max_area = shapes[0]
max_perimeter = shapes[0]
for s in shapes:
    if s.area() > max_area.area():
        max_area = s
    if s.perimeter() > max_perimeter.perimeter():
        max_perimeter = s
shape_name_area = type(max_area).__name__
shape_name_perimeter = type(max_perimeter).__name__
print(f"Max area: {max_area.area():.2f} (Shape: {shape_name_area})")
print(f"Max perimeter: {max_perimeter.perimeter():.2f} (Shape: {shape_name_perimeter})")

print("from input02.txt")
readfile("input02.txt")
max_area = shapes[0]
max_perimeter = shapes[0]
for s in shapes:
    if s.area() > max_area.area():
        max_area = s
    if s.perimeter() > max_perimeter.perimeter():
        max_perimeter = s
shape_name_area = type(max_area).__name__
shape_name_perimeter = type(max_perimeter).__name__
print(f"Max area: {max_area.area():.2f} (Shape: {shape_name_area})")
print(f"Max perimeter: {max_perimeter.perimeter():.2f} (Shape: {shape_name_perimeter})")

print("from input03.txt")
readfile("input03.txt")
max_area = shapes[0]
max_perimeter = shapes[0]
for s in shapes:
    if s.area() > max_area.area():
        max_area = s
    if s.perimeter() > max_perimeter.perimeter():
        max_perimeter = s
shape_name_area = type(max_area).__name__
shape_name_perimeter = type(max_perimeter).__name__
print(f"Max area: {max_area.area():.2f} (Shape: {shape_name_area})")
print(f"Max perimeter: {max_perimeter.perimeter():.2f} (Shape: {shape_name_perimeter})")
