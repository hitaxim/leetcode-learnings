# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        n = self.length(head)
        if k % n == 0:
            return head

        k = k % n

        node = head
        for _ in range(n - k - 1):
            node = node.next

        res = node.next
        node.next = None

        tail = res
        while tail.next:
            tail = tail.next

        tail.next = head
        return res

    def length(self, node: Optional[ListNode]) -> int:
        n = 0
        while node:
            node = node.next
            n += 1
        return n
