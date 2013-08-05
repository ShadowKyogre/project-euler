import math

def fact_sum(num):
  return sum( math.factorial(int(i)) for i in str(num) )

cnt=0
for n in range(10,math.factorial(9)*7+1):
  if fact_sum(n) == n:
    cnt+=n
