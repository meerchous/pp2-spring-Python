s = input()
t = input()
first = s.find(t)
last = s.rfind(t)
if first == last:
 print(first)
elif first == -1 :
 print()
else:
    print(str(first), str(last), sep=' ')



     
