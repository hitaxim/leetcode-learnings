# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        
        queue = deque([(1, None, root)])
        values = defaultdict(int)
        parents = defaultdict(int)
        parents[None] = root.val
        i = 0
        while True: 
            try:           
                level, _, node = queue[i]
            except:
                for level, parent, node in queue:
                    node.val = values[level] - parents[parent]
                return root
            values[level] += node.val
            if node.left:
                parents[node] += node.left.val
                queue.append((level + 1, node, node.left))
            if node.right:
                parents[node] += node.right.val
                queue.append((level + 1, node, node.right))
            i += 1
               
