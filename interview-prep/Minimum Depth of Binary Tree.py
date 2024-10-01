# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self,root):
        if root == None: 
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if root.right == None: 
            return 1 + left
        if root.left == None: 
            return right + 1
        return 1+(right if right < left else left)
        
