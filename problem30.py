ttl=0
for i in range(2,6*9**5):
  sum_digits=sum([int(x)**5 for x in str(i)])
  if i == sum_digits:
    ttl+=i
