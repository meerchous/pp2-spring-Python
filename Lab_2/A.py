s = input().split()
p = 0
for i in range(len(s)):
 p = max(i+ int(s[i]), p)
 if p <= i  and i != len(s)-1:
     print(0)
     break
else:
     print(1)
 