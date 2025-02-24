class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
            # removing digit and space from licensePlate
            licensePlate = ''.join([i.lower() for i in licensePlate if i.isalpha()])
            # sorting words array based on length of item
            words = sorted(words, key=len)
            for word in words:
                for i in range(len(licensePlate)):
                    if word.count(licensePlate[i]) < licensePlate.count(licensePlate[i]):
                        break
                    if i == len(licensePlate)-1:
                        return word

"""


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        # Step 1: Create a Counter for the letters in the licensePlate (ignore digits and spaces)
        license_counter = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        # Step 2: Find the shortest word that contains all letters from licensePlate
        def is_completing_word(word):
            word_counter = Counter(word)
            # Check if word contains all the letters with at least the frequency from licensePlate
            for char, count in license_counter.items():
                if word_counter[char] < count:
                    return False
            return True

        # Step 3: Sort words by length and check which is a completing word
        words = sorted(words, key=len)  # Sorting words by length in ascending order
        for word in words:
            if is_completing_word(word):
                return word

        return ""  # If no valid word is found, although the problem guarantees that one will exist 



"""
