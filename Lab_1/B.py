s = list(input()) 
count = 0
for i in s:
    count+=ord(i)
if count < 300:
    print('Oh, no!')
else:
    print('It is tasty!')
