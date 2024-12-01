# Write a Python program to create a class that represents a shape. Include
# methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle, and square.
import math


class Shape:
    def get_area(self):
        print("")

    def get_perimeter(self):
        print("")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

        #area A=πr2
        #Perimeter C=2πr
    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius 

class Triangle(Shape):
    def __init__(self, side_input, base_input, height_input):
        self.base = base_input
        self.height = height_input
        self.side = side_input

     #Area:   A = 1/2 × b × h
     #perimeter P=a+b+c
    def get_area(self):
        return 1/2 * self.base * self.height

    def get_perimeter(self):
        return self.side * self.base * self.height 


class Square(Shape):
    def __init__(self, side_input):
        self.side = side_input

    #Area: A=a2
    #Perimeter: P=4a 
    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4* self.side 


circleObj = Circle(5)
print(f"Circle Area: {circleObj.get_area():.2f}")
print(f"Circle Perimeter: {circleObj.get_perimeter():.2f}")


triangleObj = Triangle(3, 4, 5)
print(f"Triangle Area: {triangleObj.get_area():.2f}")
print(f"Triangle Perimeter: {triangleObj.get_perimeter():.2f}")

    
squareObj = Square(2)
print(f"Square Area: {squareObj.get_area():.2f}")
print(f"Square Perimeter: {squareObj.get_perimeter():.2f}")