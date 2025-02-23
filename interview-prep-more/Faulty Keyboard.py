class Solution:
    def finalString(self, s: str) -> str:
        result = []
        # Process each character in the input string
        for char in s:
            if char == 'i':
                # Reverse the current string when 'i' is encountered
                result.reverse()
            else:
                # Append normal characters
                result.append(char)
    return ''.join(result)
