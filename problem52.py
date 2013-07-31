from collections import Counter

cache=[Counter() for i in range(6)]

def all_same(items):
  return all(x == items[0] for x in items)

cache[0]['1']=1
num=1
while not all_same(cache):
  for idx,count in enumerate(cache):
    count.clear()
    print(num, str(num*(idx+1)))
    count.update(str(num*(idx+1)))
  num+=1
print(num-1)
