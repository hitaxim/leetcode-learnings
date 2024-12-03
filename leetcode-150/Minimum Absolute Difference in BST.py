# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)

        array = []
        while dq: 
            value = dq.popleft()
            array.append(value.val)

            if value.left: dq.append(value.left)
            if value.right: dq.append(value.right)
        
        array.sort()

        ans = float("inf")
        for i in range(1, len(array)):
            ans = min(ans, array[i] - array[i-1])
            if ans == 1: 
                break
        return ans
        
