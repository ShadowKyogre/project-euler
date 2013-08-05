import math
from collections import defaultdict

def isPrime(num):
  if num == 2: return True
  divisor=2
  while divisor < math.sqrt(num):
    if divisor % num == 0:
      return False
    divisor+=1
  else:
    return True

cache=defaultdict(lambda: bool(1))

def primeSieve(maxnum):
  sqrt=math.sqrt(maxnum)
  for i in range(2,int(sqrt)+1):
    if isPrime(i):
      j=2
      while i*j <= maxnum:
        cache[i*j]=False
        j+=1

ttl=0
primeSieve(int(2E6))
for i in range(2,int(2E6)):
  if cache[i]:
    ttl+=i
