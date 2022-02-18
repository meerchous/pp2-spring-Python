a = list(map(int, input().split()))

def return_primes(a):
    return list(filter(lambda x : prime(x),(a)))

def prime(x):
    if x == 1:
        return False
    else:
     for i in range(2,x):
         if x % i == 0:
             return False
     return True
answer = return_primes(a)
print(answer)

