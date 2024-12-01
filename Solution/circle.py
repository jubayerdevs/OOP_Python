# Write a Python program to create a class representing a Circle. Include
# methods to calculate its area and perimeter.

class Circle:
    __pi = 3.14
    def __init__(self, radius_input):
        self.radius = radius_input

    def get_area(self):
        area = (self.__pi * (self.radius** 2))
        print(f"The circle area is {area}")
    
    def get_perimeter(self):
        perimeter = 2*self.__pi*self.radius
        print(f"The circle perimeter is {perimeter}")

    

c1 = Circle(5)

c1.get_area()
c1.get_perimeter()
