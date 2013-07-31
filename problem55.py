def is_lychrel(num, max_iters=49):
  iters=0
  val=num
  revval=int(str(num)[::-1])
  while iters < max_iters:
    hold_here=val+revval
    iters+=1
    if str(hold_here)[::-1] == str(hold_here): break
    val=hold_here
    revval=int(str(val)[::-1])    
  else:
    return True
  return False

ttl=0

for i in range(1,10000):
  if is_lychrel(i):
    ttl+=1
