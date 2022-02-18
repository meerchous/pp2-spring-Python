def sentence(x):
  x.reverse()
  return ' '.join(str(i) for i in x)

s = input().split(' ')

answer = sentence(s)
print(answer)
