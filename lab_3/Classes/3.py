class Shape():

    def __init__(self,len, wid):
        self.len = int(input())
        self.wid = int(input())

    def area(self):
        print(self.len * self.wid)

class Rectangle(Shape):
    def __init__(self,len, wid):
        Shape.__init__(self,len, wid)

l = Rectangle(Shape, Shape)
l.area()