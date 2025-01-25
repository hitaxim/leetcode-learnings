class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        while True:
            if cur.next.val == 0 and cur.next.next == None:
                cur.next = None
                break

            if cur.next.val == 0:
                cur = cur.next
            
            cur.val += cur.next.val
            cur.next = cur.next.next

        return head
