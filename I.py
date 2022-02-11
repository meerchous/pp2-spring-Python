n = int(input())
for i in range(n):
 s = input()
 if '@gmail' in s:
  x = s.find('@')
  print(s[0:x])
    

