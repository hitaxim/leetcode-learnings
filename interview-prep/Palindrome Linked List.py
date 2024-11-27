### TWO POINTER 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
        
        l, r = 0, len(list_vals) -1
        while l < r and list_vals[l] == list_vals[r]:
            l += 1
            r -= 1
        return l >= r


#### USING STACK 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next
        return curr is None

#### USING RECURRSION 
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.curr = head
        return self.solve(head)

    def solve(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        ans = self.solve(head.next) and head.val == self.curr.val
        self.curr = self.curr.next
        return ans
