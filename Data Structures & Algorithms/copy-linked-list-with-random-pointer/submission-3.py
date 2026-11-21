"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None
        hMap = {}
        dummy = Node(1)
        head2 =dummy 
        run = head

        while run:
            newNode = Node(run.val)
            hMap[run] = newNode
            dummy.next = newNode
            dummy = dummy.next
            run = run.next
        
        run = head
        
        while run:
            if run.random:
                hMap[run].random = hMap[run.random]
            run = run.next
        
        return head2.next
