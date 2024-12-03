"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if i < size-1:
                    cur.next = queue[0]
                else:
                    cur.next = None
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root
