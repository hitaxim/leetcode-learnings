class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isLengthEven(self, head: ListNode) -> bool:
        current = head
        count = 0
        
        # Traverse the linked list and count the nodes
        while current:
            count += 1
            current = current.next
        
        # Return True if the count is even, otherwise False
        return count % 2 == 0

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

# Solution instantiation
solution = Solution()
result = solution.isLengthEven(head)

print(result)  # Output: True (because the length is 4, which is even)

# Creating another linked list: 1 -> 2 -> 3
head_odd = ListNode(1)
head_odd.next = ListNode(2)
head_odd.next.next = ListNode(3)

result_odd = solution.isLengthEven(head_odd)

print(result_odd)  # Output: False (because the length is 3, which is odd)
