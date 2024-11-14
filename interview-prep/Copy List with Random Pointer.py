class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: 
            return None
        maps = {}
        cur = head
        while cur: 
            maps[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur: 
            if cur.next: 
                maps[cur].next = maps[cur.next]
            if cur.random: 
                maps[cur].random = maps[cur.random]  
            cur = cur.next
        return maps[head]      
