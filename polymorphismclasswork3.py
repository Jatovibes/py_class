class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width* self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def scale(self, n):
        self.width *= n
        self.height *= n

shape = Rectangle (5, 20)      
print(shape.area())    
print(shape.perimeter())  

