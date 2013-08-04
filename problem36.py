def double_base_palindrome(num):
  #if num % 10 == 0 or num % 2 == 0: return False
  revnum=int(str(num)[::-1])
  binnum=bin(num)[2:]
  revbinnum=binnum[::-1]
  return revnum == num and binnum == revbinnum

ttl=0
for i in range(1,1000001,2):
  print(i)
  if double_base_palindrome(i): ttl+=i
