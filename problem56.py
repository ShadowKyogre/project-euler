max_sum=0

for a in range(1,101):
  for b in range(1,101):
    digit_sum=sum([int(i) for i in str(a**b)])
    if digit_sum > max_sum: max_sum=digit_sum
