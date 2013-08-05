import math

cnt=0
for n in range(1,101):
  for r in range(0,n+1):
    if math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) > 1E6:
      cnt+=1
