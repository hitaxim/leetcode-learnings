class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_h = len(haystack)
        len_n = len(needle)
        
        if len_h < len_n : 
            return -1
        for i in range(len_h):
            if haystack[i:i+len_n] == needle:
                return i

        return -1
