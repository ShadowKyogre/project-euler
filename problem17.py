from collections import Counter
DIGITS={1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine"}
TEENS={10:"ten",
       11:"eleven",
       12:"twelve",
       13:"thirteen",
       14:"fourteen",
       15:"fifteen",
       16:"sixteen",
       17:"seventeen",
       18:"eighteen",
       19:"nineteen"}
TENS={2:"twenty",
        3:"thirty",
        4:"forty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety"}
HUNDRED_FORMAT1="{} hundred"
HUNDRED_FORMAT2="{} hundred and {}"

def num2strrep(val):
  print(val)
  if val > 1000:
    return None
  elif val == 1000:
    return "one thousand"
  else:
    if val < 10:
      return DIGITS[val]
    elif val < 20:
      return TEENS[val]
    elif val < 100:
      if val % 10 == 0:
        return TENS[val//10]
      else:
        return "{} {}".format(TENS[val//10], DIGITS[val%10])
    elif val % 100 == 0:
      return HUNDRED_FORMAT1.format(DIGITS[val//100])
    else:
      return HUNDRED_FORMAT2.format(DIGITS[val//100],num2strrep(val%100))

totals=Counter()
for i in range(1,1001):
  totals.update(num2strrep(i))
ttl=0
for n in totals:
  if n == ' ':
    continue
  ttl+=totals[n]
print(ttl)
