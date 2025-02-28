## RECURSIVE APPROACH
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

## ITERATIVE SOLUTION
def factorial(n):
  answer = 1
  for i in range(1, n+1):
      answer = answer * i
  return answer
