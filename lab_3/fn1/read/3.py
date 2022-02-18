heads = 35
legs = 94
def solve(heads, legs):
  for x in range(heads+1):
       y = heads - x
       if (2*x) + (4*y) == legs:
           print(  "chickens: " + str(x), "rabbits: " + str(y))
           return x, y
solve(heads, legs)