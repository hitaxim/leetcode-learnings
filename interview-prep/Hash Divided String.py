class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = ""
        n = len(s)

        for i in range(0, n, k):
            substr = s[i:i+k]

            hash_sum = sum(ord(char) - ord('a') for char in substr)
            hash_char = hash_sum % 26
            
            res += chr(hash_char + ord('a'))
        return res
        
