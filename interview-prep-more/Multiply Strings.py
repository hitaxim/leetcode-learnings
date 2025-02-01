class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize a result array of size m + n, all zeros
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Iterate over each digit of num1 and num2 in reverse order
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply the digits at position i and j
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Calculate the current position in the result array
                p1, p2 = i + j, i + j + 1
                sum_ = mul + result[p2]
                
                # Store the sum at the correct position (mod 10) and carry over
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10
        
        # Convert the result array into a string, skipping leading zeros
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0')  # Remove leading zeros
