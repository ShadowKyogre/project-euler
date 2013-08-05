import csv
ttl=0

LETTERPOS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open('/tmp/names.txt') as f:
  for row in csv.reader(f):
    for pos,item in enumerate(sorted(row)):
      ttl+=((pos+1)*sum(LETTERPOS.index(i)+1 for i in item))
