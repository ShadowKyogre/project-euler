def integerRightTriangles(perimeter):
    solutions=set()
    #a**2+b**2=c**2
    #a+b+c=d
    #test from 45-89 degrees
    for c in range(int(perimeter*.35),int(perimeter/2)):
        for a in range(2,c):
            b=perimeter-c-a
            #print(a,b,c)
            if a+b+c == perimeter and a**2 + b**2 == c**2:
                solutions.add(frozenset([a,b,c]))
    return solutions

sol=[]
maxi=0
for i in range(120,1000):
    newsol=integerRightTriangles(i)
    if len(newsol) > len(sol):
        sol=newsol
        maxi=i

#my algorithm says 840?
