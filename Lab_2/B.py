n = int(input())
a = list(map(int, input().split()))
a.sort()
print(int(a[-1])*int(a[-2]))