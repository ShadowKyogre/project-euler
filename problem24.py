from itertools import permutations
i=0
for n in permutations("0123456789"):
  if i >= 1E6-1:
    break
  i+=1
print(n)
