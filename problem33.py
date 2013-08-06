from collections import Counter

product=1

for i in range(11,100):
  for j in range(i+1,100):
    if i == j or (i % 10 == 0 and j % 10 == 0): continue
    i_digits=Counter(int(x) for x in str(i))
    j_digits=Counter(int(x) for x in str(j))
    com_digits=i_digits&j_digits
    if len(com_digits) % 2 == 0:
      continue
    #print(i,j,i_digits,j_digits,com_digits)
    i_digits-=com_digits
    j_digits-=com_digits
    try:
      cancelled_val=list(i_digits.keys())[0]/list(j_digits.keys())[0]
    except ZeroDivisionError as e:
      continue
    if i/j == cancelled_val:
      #print(i,"/",j)
      product*=(i/j)
print(product)
