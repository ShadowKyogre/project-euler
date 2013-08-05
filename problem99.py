from math import log10
largest_n=0
nval=0

with open('/tmp/base_exp.txt') as f:
  for idx,line in enumerate(f):
    data=[float(i) for i in line.split(',')]
    val=data[1]*log10(data[0])
    if val>nval:
      largest_n=idx+1
      nval=val
