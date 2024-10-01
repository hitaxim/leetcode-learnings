# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return False
        def arrtoBT(start, end):
            if start > end: 
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = arrtoBT(start, mid-1)
            root.right = arrtoBT(mid + 1, end)
            return root
        
        return arrtoBT(0, len(nums)-1)

ORRRRRRRR

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
