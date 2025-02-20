class Solution:
    def findDifferentBinaryString(self, binaryStrings: List[str]) -> str:
        result = []

        for i in range(len(binaryStrings)):
    
            current_character = binaryStrings[i][i]

         
            result.append('1' if current_character == '0' else '0')

    
        return ''.join(result)
