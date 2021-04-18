from math import sqrt

class Shape:

    def __init__(self, length, width):
        
        self.length = length
        self.width = width

    def getLength(self):

        return self.length

    def getWidth(self):

        return self.width

class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length, self.width = length, width

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print("The perimeter of the rectangle is "+str(perimeter)+"")
        return perimeter

    def area(self):
        area = self.length * self.width
        print("The area of the rectangle is "+str(self.length * self.width)+"")
        return area

    def is_square(self):
        if self.length == self.width:
            print("This rectangle is a square of size "+str(self.getLength())+"")
            return 1
        else :
            print("This rectangle is not a square")
            return 0

class Ellipse(Shape):

    def __init__(self, MajorAxis, MinorAxis):
        self.MajorAxis, self.MinorAxis = MajorAxis, MinorAxis

    def is_circle(self):
        if self.MinorAxis==self.MajorAxis:
            print("This ellipse is a circle of radius "+str(self.MinorAxis)+"")
            return 1
        else:
            print("This ellipse is not a circle")
            return 0

    def approxArea(self):
        minArea = self.MinorAxis * self.MajorAxis / 2
        maxArea = self.MinorAxis * self.MajorAxis
        print("The area of this ellipse is between "+str(minArea)+" and "+str(maxArea)+"")
        return (minArea, maxArea)

shape1 = Rectangle(3,4)
shape2 = Ellipse(4,4)

shape2.is_circle()
shape2.approxArea()

shape1.is_square()
shape1.area()
shape1.perimeter()
