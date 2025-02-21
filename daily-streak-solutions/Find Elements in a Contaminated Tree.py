# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        
        def recover(node, val):
            if not node:
                return
            node.val = val
            self.values.add(val)
            recover(node.left, 2 * val + 1)
            recover(node.right, 2 * val + 2)
        
        recover(root, 0)
    
    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
