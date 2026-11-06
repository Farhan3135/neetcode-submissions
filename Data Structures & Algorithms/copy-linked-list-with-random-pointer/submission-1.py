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


        p = head
        nodeMap = {}

        # edge case of pointer frmo a node to None?? ?
        while p:
            
            nodeMap[p] = Node(p.val)
            if p is head:
                newHead = nodeMap[p]
            p = p.next
        
        p = head
        while p:
            copyNode = nodeMap[p]
            if p.next is None:
                copyNode.next = None
            else:
                copyNode.next = nodeMap[p.next]
            
            if p.random is None:
                copyNode.random = None
            else:
                copyNode.random = nodeMap[p.random]
            p = p.next
        
        return newHead
        