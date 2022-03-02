def selection(x,n):

    for i in range(x,n):
            yield i*i
            
a=selection(5,10)
for i in a:
    print(i, end=',')