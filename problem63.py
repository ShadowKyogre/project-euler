from math import log10
cnt=0

for i in range(1,22):
    x=1
    while x<=9:
        length=int(log10(x**i)+1)
        if length == i:
            #print(x,i,x**i)
            cnt+=1
        x+=1
