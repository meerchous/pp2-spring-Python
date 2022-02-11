n = int(input())
x = 0
while x != n:
    y=0
    while y != n:
        if x == y:
            print(x*y,end= ' ')
        elif x == 0:
            print(y,end=' ')
        elif y == 0:
            print(x , end= ' ')
        else:
            print(0,end= ' ')
        y+=1
    print(' ')
    x+=1