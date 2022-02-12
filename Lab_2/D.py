n = int(input())
x = 0
if n%2 == 0:

    while x != n:
        y = 0
        while y !=n:
            if y <= x:
                print('#',end= '')
            else:
                print('.',end='')
            y+= 1
        x+= 1
        print(' ')
else:
    while x != n:
        y = 0
        while y != n:
            if x < (n-y-1):
                print('.',end= '')
            else:
                print('#',end='')
            y+= 1
        x+= 1
        print(' ')