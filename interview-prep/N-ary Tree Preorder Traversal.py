"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def traverse(self, root, output):
        if not root: 
            return 
        
        output.append(root.val)
        for child in root.children: 
            self.traverse(child, output)
        
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        self.traverse(root, output)
        return output
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        else:
            result = [root.val]
            for child in root.children:
                result.extend(self.preorder(child))
            return result

"""
