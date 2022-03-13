import re
txt = input()
x = re.findall(r"ab", txt)
y = re.findall(r"a0", txt)
z = re.findall(r"abbb", txt)
print(x)
print(y)
print(z)