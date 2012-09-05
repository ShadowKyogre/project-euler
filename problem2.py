def fibonacchi(upToThis):
  if upToThis == 0 or upToThis == 1:
    return upToThis
  previous = 0
  secondPrevious = 1
  for i in range(upToThis):
    previous,secondPrevious=previous+secondPrevious,previous
  return previous

def main():
  total = 0
  i = 2
  while True:
    fibby =  fibonacchi(i)
    if fibby > 4E6:
      break
    else:
      if fibby % 2 == 0:
        total += fibby
    i+=1 
  print(total)

if __name__ == "__main__":
  main()
