# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                running = curr.next
                num = running.val
                while running and running.val == num:
                    running = running.next
                curr.next = running
            else:
                curr = curr.next
        
        return dummy.next
