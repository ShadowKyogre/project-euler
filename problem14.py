long_chain_cnt=0
long_chain_num=0

def collatz_chain(num):
  cnt=1
  val=num
  while val != 1:
    if val % 2 == 0:
      val/=2
    else:
      val=3*val+1
    cnt+=1
  return cnt

for i in range(1,1000000):
  cnt=collatz_chain(i)
  if cnt > long_chain_cnt:
    long_chain_cnt=cnt
    long_chain_num=i
