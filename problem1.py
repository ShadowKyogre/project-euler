def is_multiple(i, multiples):
  for n in multiples:
    if i % n == 0:
      return True
  return False

def main(*multiples):
  total = 0
  for i in range(1000):
      if is_multiple(i,multiples):
        total+=i
  return total

if __name__ == "__main__":
  print(main(3,5))
