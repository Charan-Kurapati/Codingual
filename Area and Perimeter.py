import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        circle_area = math.pi * self.radius * self.radius
        return circle_area

    def perimeter(self):
        circle_perimeter = 2 * math.pi * self.radius
        return circle_perimeter

radius = float(input("Enter the radius of circle:"))

circle = Circle(radius)

print("The radius of the circle is:",radius)
print("The area of the circle is:",round(circle.area(), 2))
print("The perimeter of the circle is:",round(circle.perimeter(),2))