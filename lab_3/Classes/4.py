class Point:
    def show(self):
        self.x1 = int(input())
        self.y1 = int(input())
        print(self.x1, self.y1)

    def move(self):
        self.x1 = int(input())
        self.y1 = int(input())
        print(self.x1, self.y1)

    def dist(self):
        self.x2 = int(input())
        self.y2 = int(input())
        d = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        print(d)

coor = Point()
coor.show()
coor.move()
coor.dist()