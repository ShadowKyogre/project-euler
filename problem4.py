val=0
for x in range(100,1000):
  for y in range(100,1000):
    prod=x*y
    if prod > val and str(prod) == str(prod)[::-1]:
      val=prod

print(val)
