n, f = map(int,input().split())
#check to prime
def prime(n):
    i = 2
    while n % i != 0:
        i += 1
    return n == i
prime(n)
if (n <= 500) and prime(n) and (f%2==0):
          print("Good job!")
else:
        print("Try next time!")
