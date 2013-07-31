from math import factorial

def digitf(num):
  total=0
  for digit in [int(i) for i in str(num)]:
    total+=factorial(digit)
  return total

def digit_chain(num):
  chain=[num]
  idx=-1
  val=digitf(num)
  while idx == -1:
    try:
      idx = chain.index(val)
    except ValueError as e:
      #print("Adding",val,"to chain,",end=" ")
      chain.append(val)
      val=digitf(val)
      #print("new value is",val)
  return chain#,idx

def chain_count(maxn=1000000, length=60):
  ttl=0
  for n in range(1,maxn):
    chain,_=digit_chain(n)
    #print(chain,idx)
    if len(chain) == length:
      ttl+=1
  return ttl
