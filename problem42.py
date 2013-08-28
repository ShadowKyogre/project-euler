import csv
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def istriseqval(num):
  solved_eq = -0.5+(0.5**2 - (2*-num))**.5
  return int(solved_eq) == solved_eq

total=0
with open('/tmp/words.txt') as f:
  for row in csv.reader(f):
    for item in row:
      value=sum([chars.index(c)+1 for c in item])
      if istriseqval(value):
        total+=1
