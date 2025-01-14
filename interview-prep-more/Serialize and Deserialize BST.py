# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        q = deque([root])
        output = []
        
        while q:
            curr = q.popleft()
            if curr:
                output.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                output.append("null")
            
        return ",".join(output)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])

        i = 1

        while q:
            curr = q.popleft()
            # Left child
            if nodes[i] != "null":
                curr.left = TreeNode(int(nodes[i]))
                q.append(curr.left)
            i += 1

            if nodes[i] != "null":
                curr.right = TreeNode(int(nodes[i]))
                q.append(curr.right)
            i += 1
        
        return root


"""
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        

        l = []

        def dfs(node):
            if node is None:
                l.append("N")
                return
            
            l.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(l)

    def deserialize(self, data: str) -> Optional[TreeNode]:
       
        data = data.split(",")
        self.i = 0

        def dfs():
            if data[self.i] == "N":
                self.i += 1
                return
            
            node = TreeNode(data[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()

"""

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
