class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters for easy manipulation
        num_list = list(str(num))
        
        # Track the last occurrence of each digit (0-9)
        last = {int(d): i for i, d in enumerate(num_list)}
        
        # Traverse the number from left to right
        for i, digit in enumerate(num_list):
            # Check for a larger digit to swap
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Swap and return the new number
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        # If no swap occurred, return the original number
        return num

  """
  class Solution:
    def maximumSwap(self, num: int) -> int:
        
        num = [int(digit) for digit in str(num)]
        
        
        def solve(num):
            if not num:
                return num
            max_num = max(num)
            if max_num == num[0]:
                return [num[0]] + solve(num[1:])
            else:
                # get the last occurance index of max element - use index() on reversed list
                index = num[::-1].index(max_num) 
				
				# add 1 to the index so that we can use the index for negetive indexing on non reversed list while swapping
                index = index+1
				
                num[0], num[-index] = num[-index], num[0]
                return num
				
        return int(''.join(str(digit) for digit in solve(num)))

  """
