
class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        # Convert lists to sets to get unique elements
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find common elements between the two sets
        common = set1.intersection(set2)
        
        # Total number of elements in each list
        n = len(nums1)
        
        # Number of unique elements in each set
        n1 = len(set1)
        n2 = len(set2)
        
        # Number of common elements
        nc = len(common)
        
        # Maximum unique elements we can keep from nums1 after removing n/2 elements
        maxUniqueNums1 = min(n1 - nc, n // 2)
        
        # Maximum unique elements we can keep from nums2 after removing n/2 elements
        maxUniqueNums2 = min(n2 - nc, n // 2)
        
        # The maximum size of the set s is the sum of the above plus the common elements
        return min(n, maxUniqueNums1 + maxUniqueNums2 + nc)


"""
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1) // 2
        A = set(nums1)
        B = set(nums2)

        # Pick from A n B and 2N - onlyA - onlyB (picks!)
        onlyA = min(len(A - B), N)
        onlyB = min(len(B - A), N)
        both = min(len(A & B), 2 * N - onlyA - onlyB)
        return onlyA + onlyB + both
"""
