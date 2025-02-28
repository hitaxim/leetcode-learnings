class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        nodes = []
        for num in nums:
            node = TreeNode(num)
            while nodes and nodes[-1].val < num:
                node.left = nodes.pop()

            if nodes:
                nodes[-1].right = node

            nodes.append(node)

        return nodes[0]
