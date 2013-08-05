bouncies=0
n=10

def is_bouncy(num):
  digits=[int(i) for i in str(num)]
  decreasing=sorted(digits)
  increasing=sorted(digits,reverse=True)
  return digits != decreasing and digits != increasing

while bouncies/n < .99:
  n+=1
  if is_bouncy(n):
    bouncies+=1
