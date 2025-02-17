class Solution:
    def countSegments(self, s: str) -> int:
        # Split the string by whitespace and count the number of resulting segments
        return len(s.split())
