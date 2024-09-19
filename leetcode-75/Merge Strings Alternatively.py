class Solution:
   def mergeAlternately(self, word1: str, word2: str) -> str:
       len1 = len(word1)
       len2 = len(word2)
       if len1 > len2 :
           big_str = word1
       elif len2 > len1 :
           big_str = word2
       max_len = max(len1, len2)
       min_len = min(len1, len2)
       str_ans = ""
       for i in range(max_len):
           if i <= min_len-1:
               str_ans += word1[i]
               str_ans += word2[i]
           else:
               str_ans += big_str[i]

       return str_ans
