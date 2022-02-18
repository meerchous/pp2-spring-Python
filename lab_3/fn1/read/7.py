def has_33(x):
    for i in range(len(x)-1):
      a = False
      if int(x[i]) == 3 and int(x[i+1]) == 3:
         a = True
         break       
    print(a)

x = input().split()
has_33(x)

