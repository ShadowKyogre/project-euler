def factors(num,include_self=True):
    divisors=[1,]
    if include_self:
        divisors.append(num)
    for n in range(2,int(num/2)+1):
        if num % n == 0:
            divisors.append(n)
    return divisors

def trianglenum(num):
    return ((num)*(num+1))/2

"""
#12
targetnum=0
for n in range(1000,2000):
    if len(factors(trianglenum(n))) > 500:
        targetnum=n
        break

print(targetnum)
"""

#21
amicables=set()
for i in range(2,10000):
    if i in amicables: continue
    other_i=sum(factors(i, include_self=False))
    if other_i != i and sum(factors(other_i, include_self=False)) == i:
        amicables.add(other_i)
        amicables.add(i)
print(sum(amicables), amicables)
#sum is 31626? {1184, 6368, 284, 5020, 2924, 6232, 1210, 5564, 220, 2620}
