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

def truncatablePrime(num, r2l=False):
  digits = list(str(num))
  if '1' == digits[0] or '1' == digits[-1]: return False
  pophere=-1 if r2l else 0
  digits.pop(pophere)
  while len(digits) > 0:
    #print(digits)
    if not cache[int(''.join(digits))]:
      return False
    digits.pop(pophere)
  else:
    return True

primeSieve(int(1E6))
ttl=0
for i in range(11,int(1E6)):
  if cache[i] and truncatablePrime(i) and truncatablePrime(i,r2l=True):
      ttl+=i
