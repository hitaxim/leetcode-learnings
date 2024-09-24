class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for n in nums[1:]:
            if n < 0: 
                max_product, min_product = min_product, max_product
            
            max_product = max(n, n * max_product)
            min_product = min(n, n * min_product)

            result = max(max_product, result)
        return result
