def contains_duplicate(input):
  input.sort()
  for i in range(len(input)-1):
      if (input[i] == input[i+1]):
          return True
  return False

def contains_duplicate(input):
  seen = {}
  for i in input:
    if i in seen:
      return True
    seen[i] = True
  return False
