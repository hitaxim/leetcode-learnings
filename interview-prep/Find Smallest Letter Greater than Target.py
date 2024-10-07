class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect_right(letters, target)
        if idx < len(letters):
            return letters[idx]
        else: 
            return letters[0]
        
