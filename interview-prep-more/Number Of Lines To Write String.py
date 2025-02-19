class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        total_lines = 1
        current_width = 0
        
        for char in s:
            char_index = ord(char) - ord('a')  # Get the index of the character
            char_width = widths[char_index]     # Get the width of the character
            
            if current_width + char_width > 100:
                total_lines += 1      # Move to the next line
                current_width = char_width  # Start the new line with the current character width
            else:
                current_width += char_width  # Add to the current line width
        
        return [total_lines, current_width]

   
