class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root.left:
            return -1

        nodes_queue = deque([root])
        second_min = float('inf')
        min_val = root.val

        while nodes_queue:
            current_node = nodes_queue.popleft()

            if current_node.left:
                nodes_queue.append(current_node.left)
                nodes_queue.append(current_node.right)

                if current_node.left.val > min_val:
                    second_min = min(second_min, current_node.left.val)

                if current_node.right.val > min_val:
                    second_min = min(second_min, current_node.right.val)

        return -1 if second_min == float('inf') else second_min
