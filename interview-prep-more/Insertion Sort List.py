# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        x=[]
        temp=head
        while temp!=None:
            x.append(temp.val)
            temp=temp.next
        x.sort()
        temp=head
        for i in x:
            temp.val=i
            temp=temp.next
        return head
