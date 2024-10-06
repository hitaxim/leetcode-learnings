# Python3 program to find Majority
# element in an array using nested loops

# Function to find the Majority element in an array
def majorityElement(arr):
    n = len(arr)  

    # Loop to consider each element as a candidate for majority
    for i in range(n):
        count = 0

        # Inner loop to count the frequency of arr[i]
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1

        # Check if count of arr[i] is more than half the size of the array
        if count > n // 2:
            return arr[i]

    # If no majority element found, return -1
    return -1



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        n = len(nums)
        for x in nums: 
            seen[x] = seen.get(x,0) + 1
            if seen[x] > n // 2:
                return x
        
       
