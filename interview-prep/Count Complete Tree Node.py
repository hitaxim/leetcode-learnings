# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        h = 0
        while root: 
            h += 1
            root = root.left
        return h

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        ld = self.depth(root.left)
        rd = self.depth(root.right)

        if ld == rd:
            return 1 + ((2 ** ld) - 1) + self.countNodes(root.right)
        else: 
            return 1 + ((2 ** rd) - 1) + self.countNodes(root.left)
        
