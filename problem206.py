import re
import math
get_this=re.compile(r"1\d2\d3\d4\d5\d6\d7\d8\d9\d0")
not_fulfilled = True
num=1010101010
while not_fulfilled and num <= 1389026623:
  sq=num**2
  #print(num)
  if get_this.match(str(sq)):
    not_fulfilled=False
  else:
    num+=10
