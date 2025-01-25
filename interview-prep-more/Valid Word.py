class Solution:
  def isValid(self, word: str) -> bool:
    if len(word) < 3:
      return False

    vowel_map = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    vowel, consonant = False, False

    for char in word:
      if char in vowel_map:
        vowel = True
      elif char.isalpha():  # Check for alphabets
        consonant = True
      elif char.isdigit():  # Check for digits
        continue
      else:
        return False

    return vowel and consonant
