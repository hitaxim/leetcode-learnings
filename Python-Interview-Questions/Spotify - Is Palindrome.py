def isPalindrome(phrase):
  l = 0
  r = len(phrase) - 1
  
  while l < r:
    if not phrase[l].isalnum():
      l += 1
      continue
    if not phrase[r].isalnum():
      r -= 1
      continue
    if phrase[l].lower() == phrase[r].lower():
      l += 1
      r -= 1
    else:
      return False
  return True
