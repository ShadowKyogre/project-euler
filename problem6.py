def squared_sum(maxnum):
  total=0
  for n in range(1,maxnum+1):
    total+=n
  return total**2

def sum_of_squares(maxnum):
  total=0
  for n in range(1,maxnum+1):
    total+=n**2
  return total

print(squared_sum(100)-sum_of_squares(100))
