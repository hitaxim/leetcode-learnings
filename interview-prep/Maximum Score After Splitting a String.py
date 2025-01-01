class Solution:
    def maxScore(self, s: str) -> int:
        max_score = count_zeros_left = 0
        count_ones_right = s.count('1')

        for i in range(len(s) - 1):
            if s[i] == '0':
                count_zeros_left += 1
            if s[i] == '1':
                count_ones_right -= 1
            max_score = max(max_score, count_ones_right + count_zeros_left)
        
        return max_score
