import math
n, l = map(int, input().split())
area = 0.25*l*l*n/(math.tan((math.pi)/n))
print(area)