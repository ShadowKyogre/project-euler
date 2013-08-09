from itertools import permutations

def isPrime(num):
    if num == 2: return True
    for i in range(2,int(num**.5)):
        if num % i == 0:
            return False
    return True

EVENS={'2','4','6','8'}
TEST_THESE=[]
#1-3 pandigital
TEST_THESE.extend(list(int(''.join(x)) for x in permutations('123')))
#1-4 pandigital
TEST_THESE.extend(list(int(''.join(x)) for x in permutations('1234')))
#1-5 pandigital
TEST_THESE.extend(list(int(''.join(x)) for x in permutations('12345')))
#1-6 pandigital
TEST_THESE.extend(list(int(''.join(x)) for x in permutations('123456')))
#1-7 pandigital
TEST_THESE.extend(list(int(''.join(x)) for x in permutations('1234567')))
#1-8 pandigital
TEST_THESE.extend(list(int(''.join(x)) for x in permutations('12345678')))
#1-9 pandigital
TEST_THESE.extend(list(int(''.join(x)) for x in permutations('123456789')))

TEST_THESE=filter(lambda x: str(x%10) not in EVENS, TEST_THESE)

largest_val=0
for i in TEST_THESE:
    if i>largest_val and isPrime(i):
        largest_val=i

#7652413
