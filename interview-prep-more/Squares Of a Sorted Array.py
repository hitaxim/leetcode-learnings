class Solution:
    def getMax(self, arr):
        max_val = max(arr)
        return max_val

    def countSort(self, arr, exp):
        output = [0] * len(arr)
        count = [0] * 10

        for num in arr:
            count[(num // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            output[count[(arr[i] // exp) % 10] - 1] = arr[i]
            count[(arr[i] // exp) % 10] -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

    def radixSort(self, arr):
        max_val = self.getMax(arr)

        exp = 1
        while max_val // exp > 0:
            self.countSort(arr, exp)
            exp *= 10

    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        self.radixSort(nums)
        return nums
