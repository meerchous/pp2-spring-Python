class Shape():
    
    def __init__(self,len):
        self.len = int(input())

    def area(self):
        print(self.len**2)

class Square(Shape):
    def __init__(self,len):
        Shape.__init__(self,len)

l = Square(Shape)
l.area()